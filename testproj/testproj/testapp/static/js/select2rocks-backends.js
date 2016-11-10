/**
 * Extend list of Select2 backends.
 *
 */
(function ($) {
    "use strict";

    $.extend(true, $.fn.Select2RocksBackends, {
      tastypie: {
        ajax: {
          dataType: 'json',
          data: function (term, page) {
            return {name__icontains: term};
          },
          results: function (data, page) {
            return {results: data.objects};
          }
        },
        formatResult: function(item) {
          return item.name;
        },
        formatSelection: function(item) {
          // Handle restored form
          if (item.restored) {
            return item.text;
          } else {
            return item.name;
          }
        }
      },
      restframework: {
        ajax: {
          dataType: 'json',
          data: function (term, page) {
            return {search: term};
          },
          results: function (data, page) {
            // No .objects as in tastypie backend
            return {results: data};
          }
        },
        formatResult: function(item) {
          return item.name;
        },
        formatSelection: function(item) {
          // Handle restored form
          if (item.restored) {
            return item.text;
          } else {
            return item.name;
          }
        }
      }
    });
})(jQuery);
