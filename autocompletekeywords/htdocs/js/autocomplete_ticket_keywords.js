jQuery(document).ready(function($) {
    $("#field-keywords").autocomplete("../ac-keywords", {
        cacheLength: 3,
        minChars: 2,
        multiple: true,
        delay: 100
    } ); 
});
