<?php

include_once 'Voice.php';

$voice = $_GET['voice'] ?: null;
$text = $_GET['text'] ?: null;
$name = $_GET['name'] ?: null;
$scale = $_GET['scale'] ?: null;

if (empty($_GET)) die("It works! You can use such GET parameters to generate a speech: voice, text, name. Example: <a href=\"/?text=Привет+Мир!&voice=Aleksandr\">text=Привет+Мир!&voice=Aleksandr</a>");

$voice = (new Voice($text, $voice, $name, $scale))->createVoice()->streamVoice();

/*
 * Після кожного запиту видаляємо озвучений файл
 */
register_shutdown_function('unlink', $voice->getOutFileName());