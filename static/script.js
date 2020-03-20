$(function() {
  const BASE_URL = "http://localhost:5000/"
  $submitButton = $('#submit');
  $guessInput = $('#guess');
  $result = $('#result');

  $submitButton.on('click', async function(e){
    e.preventDefault();

    let guess = $guessInput.val();
    let response = await axios.get(`${BASE_URL}/make-guess?guess=${guess}`);

    // display result from JSON response
    $result.text(response.data.result)
  });
});
