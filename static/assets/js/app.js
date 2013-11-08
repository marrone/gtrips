var app = app || {};

$(function() {
    $(".date-picker").datepicker(); //({dateFormat: "D, M d, yy"});

    $(".page-jumpto").change(function(e) {
        e.preventDefault();
        var pageNum = parseInt(this.options[this.selectedIndex].value, 10);
        if(pageNum) {
            window.location = this.form.action + "?page=" + pageNum;
        }
    });

});
