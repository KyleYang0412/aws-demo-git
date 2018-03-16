$(document).ready(function(){

    $("button#GET").click(function(){
        $.ajax({
        	url:'https://lbj6o6vqhc.execute-api.us-east-2.amazonaws.com/RDSTest/rdstest',
          type: 'GET'
        }).done(function(ret){
        	console.log(ret);
        	$('#display-area').html( JSON.stringify(ret));
        });
    });

    $("button#POST").click(function(){
    		var inputName = $('input#post-input-name').val();
        var inputID = $('input#post-input-id').val();

        $.ajax({
        	url:'https://lbj6o6vqhc.execute-api.us-east-2.amazonaws.com/RDSTest/rdstest',
          type: 'POST',
          data: JSON.stringify({"newEmpID":inputID,"newName":inputName})
        }).done(function(ret){
        	console.log(ret);
        	$('#display-area').html( JSON.stringify(ret));
        });
    });
    
    $("button#DELETE").click(function(){
        var deleteID = $('input#delete-input-id').val();

        $.ajax({
        	url:'https://lbj6o6vqhc.execute-api.us-east-2.amazonaws.com/RDSTest/rdstest',
          type: 'DELETE',
          data: JSON.stringify({"newEmpID":deleteID})
        }).done(function(ret){
        	console.log(ret);
        	$('#display-area').html( JSON.stringify(ret));
        });
    });
});
