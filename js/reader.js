(function () {
  'use strict';

  /* ── Constants ────────────────────────────────────────────────────── */
  var TOTAL_PAGES = 1098;
  var ZOOM_LEVELS = [70, 80, 90, 100, 110, 120, 130, 140];
  var LS_PAGE = 'ml-reader-page';
  var LS_VIEW = 'ml-reader-view';
  var LS_ZOOM = 'ml-reader-zoom';

  /* ── State ────────────────────────────────────────────────────────── */
  var currentPage = 1;
  var viewMode = 'image';   // 'image' | 'text'
  var zoomLevel = 100;
  var contextMenuOpen = false;

  /* ── DOM cache ────────────────────────────────────────────────────── */
  var els = {};

  function cacheDom() {
    els.pageCounter   = document.getElementById('page-counter');
    els.pageDisplay   = document.getElementById('page-display');
    els.imageView     = document.getElementById('image-view');
    els.textView      = document.getElementById('text-view');
    els.textContent   = document.getElementById('text-content');
    els.pageImage     = document.getElementById('page-image');
    els.btnPrev       = document.getElementById('btn-prev');
    els.btnNext       = document.getElementById('btn-next');
    els.pageInput     = document.getElementById('page-input');
    els.progressBar   = document.getElementById('progress-bar');
    els.zoomPanel     = document.getElementById('zoom-panel');
    els.openNewTab    = document.getElementById('open-new-tab');
    els.contextFab    = document.getElementById('context-fab');
    els.contextMenu   = document.getElementById('context-menu');
    els.ctxPrev       = document.getElementById('ctx-prev');
    els.ctxNext       = document.getElementById('ctx-next');
    els.ctxPageLabel  = document.getElementById('ctx-page-label');
    els.ctxToggleView = document.getElementById('ctx-toggle-view');
    els.ctxClose      = document.getElementById('ctx-close');
    els.searchInput   = document.getElementById('search-input');
    els.searchResults = document.getElementById('search-results');
  }

  /* ── Helpers ──────────────────────────────────────────────────────── */

  function pad(n) {
    return String(n).padStart(4, '0');
  }

  function imagePath(page) {
    return 'pages/page-' + pad(page) + '.jpg';
  }

  function textPath(page) {
    return 'text/page_' + pad(page) + '.html';
  }

  function clamp(val, min, max) {
    return Math.max(min, Math.min(max, val));
  }

  /* ── Persistence ─────────────────────────────────────────────────── */

  function saveState() {
    try {
      localStorage.setItem(LS_PAGE, String(currentPage));
      localStorage.setItem(LS_VIEW, viewMode);
      localStorage.setItem(LS_ZOOM, String(zoomLevel));
    } catch (e) {
      // localStorage unavailable — silently ignore
    }
  }

  function loadState() {
    try {
      var savedPage = parseInt(localStorage.getItem(LS_PAGE), 10);
      if (!isNaN(savedPage)) currentPage = clamp(savedPage, 1, TOTAL_PAGES);

      var savedView = localStorage.getItem(LS_VIEW);
      if (savedView === 'image' || savedView === 'text') viewMode = savedView;

      var savedZoom = parseInt(localStorage.getItem(LS_ZOOM), 10);
      if (!isNaN(savedZoom) && ZOOM_LEVELS.indexOf(savedZoom) !== -1) zoomLevel = savedZoom;
    } catch (e) {
      // localStorage unavailable — use defaults
    }
  }

  /* ── URL parameter helpers ───────────────────────────────────────── */

  function parseUrlPage() {
    var params = new URLSearchParams(window.location.search);
    var p = parseInt(params.get('page'), 10);
    if (!isNaN(p)) {
      currentPage = clamp(p, 1, TOTAL_PAGES);
    }
  }

  function updateUrlParam() {
    var url = new URL(window.location);
    url.searchParams.set('page', String(currentPage));
    window.history.replaceState(null, '', url.toString());
  }

  /* ── Page navigation ─────────────────────────────────────────────── */

  function goToPage(page) {
    page = clamp(page, 1, TOTAL_PAGES);
    currentPage = page;

    // Update page counter
    els.pageCounter.textContent = 'Pagina ' + currentPage + ' din ' + TOTAL_PAGES;

    // Update page input
    els.pageInput.value = currentPage;

    // Update context menu page label
    els.ctxPageLabel.textContent = 'Pagina ' + currentPage;

    // Update progress bar
    var pct = ((currentPage - 1) / (TOTAL_PAGES - 1)) * 100;
    els.progressBar.style.width = pct + '%';

    // Update button states
    els.btnPrev.disabled = currentPage === 1;
    els.btnNext.disabled = currentPage === TOTAL_PAGES;
    els.ctxPrev.disabled = currentPage === 1;
    els.ctxNext.disabled = currentPage === TOTAL_PAGES;

    // Show the correct view
    if (viewMode === 'image') {
      showImageView();
    } else {
      showTextView();
    }

    // Update "open in new tab" link
    els.openNewTab.href = imagePath(currentPage);

    // Save state
    saveState();
    updateUrlParam();
  }

  /* ── Image view ──────────────────────────────────────────────────── */

  function showImageView() {
    els.imageView.style.display = '';
    els.textView.style.display = 'none';
    els.pageImage.src = imagePath(currentPage);
    els.pageImage.alt = 'Pagina ' + currentPage;
  }

  /* ── Text view ───────────────────────────────────────────────────── */

  function showTextView() {
    els.imageView.style.display = 'none';
    els.textView.style.display = '';
    fetchTextContent(currentPage);
  }

  function fetchTextContent(page) {
    els.textContent.innerHTML = '<p class="loading-text">Se incarca textul...</p>';

    fetch(textPath(page))
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.text();
      })
      .then(function (html) {
        // Only update if we are still on the same page
        if (currentPage === page) {
          els.textContent.innerHTML = html;
        }
      })
      .catch(function () {
        if (currentPage === page) {
          els.textContent.innerHTML =
            '<p class="error-text">Textul nu este disponibil pentru aceasta pagina.</p>';
        }
      });
  }

  /* ── Toggle view ─────────────────────────────────────────────────── */

  function toggleView() {
    if (viewMode === 'image') {
      viewMode = 'text';
      els.ctxToggleView.textContent = 'Comuta la Vizualizare Imagine';
      showTextView();
    } else {
      viewMode = 'image';
      els.ctxToggleView.textContent = 'Comuta la Vizualizare Text';
      showImageView();
    }
    saveState();
  }

  /* ── Zoom ─────────────────────────────────────────────────────────── */

  function setZoom(level) {
    zoomLevel = level;

    // Apply transform
    var scale = level / 100;
    els.pageDisplay.style.transform = 'scale(' + scale + ')';
    els.pageDisplay.style.transformOrigin = 'top center';

    // Update active button
    var btns = els.zoomPanel.querySelectorAll('.zoom-btn');
    for (var i = 0; i < btns.length; i++) {
      var btn = btns[i];
      var z = parseInt(btn.getAttribute('data-zoom'), 10);
      if (z === level) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }

    saveState();
  }

  /* ── Context menu ────────────────────────────────────────────────── */

  function openContextMenu() {
    contextMenuOpen = true;
    els.contextMenu.style.display = '';
    els.searchInput.value = '';
    els.searchResults.innerHTML = '';
  }

  function closeContextMenu() {
    contextMenuOpen = false;
    els.contextMenu.style.display = 'none';
  }

  function toggleContextMenu() {
    if (contextMenuOpen) {
      closeContextMenu();
    } else {
      openContextMenu();
    }
  }

  /* ── Search ──────────────────────────────────────────────────────── */

  var searchDebounceTimer = null;

  function performSearch(query) {
    els.searchResults.innerHTML = '';

    if (!query || query.length < 2) return;
    if (!window.pagesData || !Array.isArray(window.pagesData)) return;

    var lower = query.toLowerCase();
    var matches = [];

    for (var i = 0; i < window.pagesData.length && matches.length < 8; i++) {
      var entry = window.pagesData[i];
      var title = (entry.title || '').toLowerCase();
      var text = (entry.searchText || '').toLowerCase();
      if (title.indexOf(lower) !== -1 || text.indexOf(lower) !== -1) {
        matches.push(entry);
      }
    }

    if (matches.length === 0) {
      els.searchResults.innerHTML =
        '<li class="search-no-results">Niciun rezultat gasit.</li>';
      return;
    }

    matches.forEach(function (entry) {
      var li = document.createElement('li');
      li.className = 'search-result-item';
      li.innerHTML =
        '<span class="result-page">p.' + entry.page + '</span>' +
        '<span class="result-title">' + escapeHtml(entry.title || 'Fara titlu') + '</span>';
      li.addEventListener('click', function () {
        goToPage(entry.page);
        closeContextMenu();
      });
      els.searchResults.appendChild(li);
    });
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  /* ── Keyboard navigation ─────────────────────────────────────────── */

  function handleKeydown(e) {
    // Don't capture keys when typing in inputs
    var tag = e.target.tagName.toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select') return;

    switch (e.key) {
      case 'ArrowLeft':
      case 'a':
      case 'A':
        e.preventDefault();
        goToPage(currentPage - 1);
        break;

      case 'ArrowRight':
      case 'd':
      case 'D':
        e.preventDefault();
        goToPage(currentPage + 1);
        break;

      case 'Home':
        e.preventDefault();
        goToPage(1);
        break;

      case 'End':
        e.preventDefault();
        goToPage(TOTAL_PAGES);
        break;

      case 'Escape':
        if (contextMenuOpen) {
          e.preventDefault();
          closeContextMenu();
        }
        break;

      case 't':
      case 'T':
        e.preventDefault();
        toggleView();
        break;

      case 'm':
      case 'M':
        e.preventDefault();
        toggleContextMenu();
        break;
    }
  }

  /* ── Preload adjacent pages ──────────────────────────────────────── */

  function preloadAdjacentPages() {
    var pagesToPreload = [currentPage - 1, currentPage + 1, currentPage + 2];
    for (var i = 0; i < pagesToPreload.length; i++) {
      var p = pagesToPreload[i];
      if (p >= 1 && p <= TOTAL_PAGES) {
        var img = new Image();
        img.src = imagePath(p);
      }
    }
  }

  /* ── Event binding ───────────────────────────────────────────────── */

  function bindEvents() {
    // Previous / Next buttons
    els.btnPrev.addEventListener('click', function () {
      goToPage(currentPage - 1);
    });

    els.btnNext.addEventListener('click', function () {
      goToPage(currentPage + 1);
    });

    // Page input
    els.pageInput.addEventListener('change', function () {
      var val = parseInt(els.pageInput.value, 10);
      if (!isNaN(val)) goToPage(val);
    });

    els.pageInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        var val = parseInt(els.pageInput.value, 10);
        if (!isNaN(val)) goToPage(val);
        els.pageInput.blur();
      }
    });

    // Zoom buttons
    var zoomBtns = els.zoomPanel.querySelectorAll('.zoom-btn');
    for (var i = 0; i < zoomBtns.length; i++) {
      zoomBtns[i].addEventListener('click', function () {
        var z = parseInt(this.getAttribute('data-zoom'), 10);
        if (!isNaN(z)) setZoom(z);
      });
    }

    // Context menu FAB
    els.contextFab.addEventListener('click', function (e) {
      e.stopPropagation();
      toggleContextMenu();
    });

    // Context menu close button
    els.ctxClose.addEventListener('click', function () {
      closeContextMenu();
    });

    // Context menu navigation
    els.ctxPrev.addEventListener('click', function () {
      goToPage(currentPage - 1);
    });

    els.ctxNext.addEventListener('click', function () {
      goToPage(currentPage + 1);
    });

    // Context menu toggle view
    els.ctxToggleView.addEventListener('click', function () {
      toggleView();
    });

    // Click overlay background to close
    els.contextMenu.addEventListener('click', function (e) {
      if (e.target === els.contextMenu) {
        closeContextMenu();
      }
    });

    // Search input
    els.searchInput.addEventListener('input', function () {
      var query = els.searchInput.value.trim();
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(function () {
        performSearch(query);
      }, 300);
    });

    // Search result clicks
    els.searchResults.addEventListener('click', function (e) {
      var item = e.target.closest('.search-result-item');
      if (item) {
        var page = parseInt(item.getAttribute('data-page'), 10);
        if (!isNaN(page)) {
          goToPage(page);
          closeContextMenu();
        }
      }
    });

    // Keyboard navigation
    document.addEventListener('keydown', handleKeydown);

    // Preload adjacent pages after current page loads
    els.pageImage.addEventListener('load', function () {
      preloadAdjacentPages();
    });

    // Touch / swipe support
    var touchStartX = 0;
    var touchStartY = 0;
    var touchEndX = 0;
    var touchEndY = 0;
    var minSwipeDistance = 50;

    els.pageDisplay.addEventListener('touchstart', function (e) {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });

    els.pageDisplay.addEventListener('touchend', function (e) {
      touchEndX = e.changedTouches[0].screenX;
      touchEndY = e.changedTouches[0].screenY;

      var dx = touchEndX - touchStartX;
      var dy = touchEndY - touchStartY;

      // Only trigger if horizontal swipe is dominant
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > minSwipeDistance) {
        if (dx > 0) {
          goToPage(currentPage - 1); // Swipe right = previous
        } else {
          goToPage(currentPage + 1); // Swipe left = next
        }
      }
    }, { passive: true });

    // Progress bar click to jump to page
    var progressTrack = document.querySelector('.progress-bar-track');
    if (progressTrack) {
      progressTrack.addEventListener('click', function (e) {
        var rect = progressTrack.getBoundingClientRect();
        var ratio = (e.clientX - rect.left) / rect.width;
        var page = Math.round(ratio * (TOTAL_PAGES - 1)) + 1;
        goToPage(page);
      });
    }

    // Handle browser back/forward
    window.addEventListener('popstate', function () {
      parseUrlPage();
      goToPage(currentPage);
    });
  }

  /* ── Initialization ──────────────────────────────────────────────── */

  function init() {
    cacheDom();
    loadState();
    parseUrlPage();

    // Set initial toggle button text based on view mode
    if (viewMode === 'text') {
      els.ctxToggleView.textContent = 'Comuta la Vizualizare Imagine';
    } else {
      els.ctxToggleView.textContent = 'Comuta la Vizualizare Text';
    }

    setZoom(zoomLevel);
    bindEvents();
    goToPage(currentPage);
  }

  /* ── Boot ─────────────────────────────────────────────────────────── */

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
