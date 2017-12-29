/* php script for intercepting the HTTP requests from intercept_index.php */
/* by s3t3bo55 */

<?php
$req_dump = print_r($_REQUEST, TRUE);
$fp = fopen('request.log', 'a');
fwrite($fp, $req_dump);
fclose($fp);
?>
