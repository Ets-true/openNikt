<?php
    $name =$_POST['name']
    $phone =$_POST['phone']
    $email =$_POST['email']
    $message =$_POST['message']
    $token="1872010706:AAG1GrVYhIV6iYUe5BTl1AIgV6QS4738NVw"
    $chat_id="-528140504"
    $arr = array(
        'Имя клиента: ' => $name,
        'Телефон: ' => $phone,
        'Email: ' => $email,
        'Текст сообщения: ' => $message
    );
    foreach($arr as $key  => $value) {
        $txt .= "<b>".$key."</b> ".$value."%0A";
    }
    $sendToTelegram = fopen("https://api.telegram.org/bot{$token}/sendMessage?chat_id={$chat_id}
        &parse_mode=html&text={$txt}", "r");
    if ($sendToTelegram){
        echo '<h1 class="success"> Ваше сообщение отправлено </hi>';
        return true;
    } else {
        echo "Error";
    }
?>