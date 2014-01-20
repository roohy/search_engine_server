/**
 * Created by roohy on 1/15/14.
 */

function sendToserver(){
    var ajaxData = {
        searchTerm : $('#searchTerm').val(),
    };
    var url = '/ajax/search/';
    $('#resultContainer').html("");
	$.ajax({
		url: url,
		type: 'POST',
//		dataType: 'json',
		data: ajaxData,
		success: function(data, status, xhr){

            if (data){
                console.log(data);
                var label_temp = $('<div class="yellow ui message result_count">'+data.length+' Results Retrived</div>');
                label_temp.insertAfter('#search_header');
                label_temp.slideDown(400,function(){

                    setTimeout(function(){
                        label_temp.slideUp(400,function(){
                            label_temp.remove();
                        })
                        }, 1000);
                });
                for (var i = 0 ; i<data.length ; i++)
                {
                    $('<div class="ui segment search-result"><p><b>'+data[i].url +'</b><br/>'+ data[i].title +
                        '</p><div class="ui label blue ranks">Rank<div class="detail">'+ data[i].rank +
                        '</div></div></div>').appendTo('#resultContainer');
                }
                $('.search-result').hover(function(e){
                   $( e.target).children('.ranks').slideDown();
                },function(e){
                    $(e.target).children('.ranks').slideUp();
                });
		       // Request error
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
