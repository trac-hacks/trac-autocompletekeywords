jQuery(document).ready(function($) {
    $("#field-keywords").autocomplete(KEYWORDS_AC_PATH, {
        cacheLength: 3,
        minChars: 2,
        multiple: true,
        multipleSeparator: " ",
        delay: 100
    } ); 
});
