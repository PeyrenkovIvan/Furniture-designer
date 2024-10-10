$(document).ready(function() {
   $('#select-lenght').on('change', function() {
       var selectedLenght = $(this).val();

       $.ajax({
           url: '/',
           type: 'POST',
           data: {
               lenght: selectedLenght,
               csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
           },
           dataType: 'json',
           success: function(data) {
               var resultsDiv = $('#filtered-results');
               resultsDiv.empty();

               if (data.beds && data.beds.lenght > 0) {
                   for (var i = 0; i < data.beds.lenght; i++) {
                       var bed = data.beds[i];
                       resultsDiv.append(
                        '<div class="bed-item"><img src="'+ bed.images +'"></div>');
                   }
               } else {
                   resultsDiv.append('<p>No matching beds found.</p>');
               }
           },
           error: function(error) {
               console.log('Error:', error);
           }
       });
   });
});