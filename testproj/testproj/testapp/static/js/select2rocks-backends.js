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
        initSelection: function(element, callback) {
          var elt = $(element);
          var data = {id: elt.val(), name: elt.data('text')};
          callback(data);
        },
        formatResult: function(item) {
	  return item.name;
	},
	formatSelection: function(item) {
	  return item.name;
	}
      },
      restframework: {
        ajax: {
          dataType: 'json',
          data: function (term, page) {
	    return {name__icontains: term};
	  },
	  results: function (data, page) {
            // No .objects as in tastypie backend
	    return {results: data};
	  }
        },
        initSelection: function(element, callback) {
          var elt = $(element);
          var data = {id: elt.val(), name: elt.data('text')};
          callback(data);
        },
        formatResult: function(item) {
	  return item.name;
	},
	formatSelection: function(item) {
	  return item.name;
	}
      }
    });
})(jQuery);
