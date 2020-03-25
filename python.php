<?php

$call_url = 'http://localhost:5000/PredictData?param1=' . urlencode('Best website for Write Name Online Greeting Wish Card Cool Profile Picture Free. Write name on birthday cakes birthday wishes.');

$cURLConnection = curl_init();

curl_setopt($cURLConnection, CURLOPT_URL, $call_url);
curl_setopt($cURLConnection, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($cURLConnection);
curl_close($cURLConnection);

echo "<pre>";
	print_r($call_url);
	echo "<br/>";
	echo "<br/>";
	print_r($result);
echo "</pre>";

?>
