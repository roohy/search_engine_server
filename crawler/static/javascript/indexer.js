/**
 * Created by roohy on 1/15/14.
 */

function sendToserver(){
    var ajaxData = {
        url: $('#urlInput').val(),
        count: $('#countInput').val()
    };
    var url = '/ajax/index/';

	$.ajax({
		url: url,
		type: 'POST',
//		dataType: 'json',
		data: ajaxData,
		success: function(data, status, xhr){
		    if (data){
                console.log("eyvayyy");
                $('#rankTable').slideDown();
                $('#rankTableBody').html('');
                for ( var i in data){
                   $('<tr><td>' + data[i].url + '</td><td>' + data[i].rank + '</td></tr>').appendTo("#rankTableBody") ;
               }
		    }else {
		       // success
		    }
		}
		// ...
	});

    $('#progressBar').show();
    $('#progressBar div').animate({
        width: '100%'
    },5000,function(){
        //on complete

        $('#progressBar').addClass('successful');
    });
}

$(document).ready(function(){
    $('#progressBar').hide();
    $('#indexButton').click(sendToserver);
});

/*

	var ajaxData = {
	  category: 2,
	  search: "Madness",
	  page: 1
	}

	var url = "http://webproject.roohy.me/ajax/1/me/product/list";

	$.ajax({
		url: url,
		type: 'post',
		dataType: 'json',
		data: ajaxData,
		success: function(data, status, xhr){
		    if (data.result == 0){
		       // Request error
		    }else {
		       // success
		    }
		},
		// ...
	});
 */