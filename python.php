<?php

$string = isset($_GET['param1'])? urlencode($_GET['param1']) : 'name';

$call_url = 'http://localhost:5000/PredictData?param1=' . $string;

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
