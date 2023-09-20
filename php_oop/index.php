<?php

class fruit
{
    ///properties
    public $name; /// setzt die variablen die als Platzhalter benutz werden um die funktionen zu benutzen
    public $color;


    ///methods
    function set_name($name) // setzt diese methode die variable name 
    {
        $this->name = $name; /// setzt die funktion in der methode
    } /// beendet die funktion

    function get_name() /// hier muss kein platzhalter gesetzt werden da der wert hier nur ausgegeben wird.
    {
        return $this->name; ///gibt die methode aus mit der modifizierung von $name oben in set_name
    }

    function set_color($color){
        $this->color = $color;
    }

    function get_color(){

        return $this->color; 

    }
}


$apple = new fruit();


$apple->set_name('Apple');
$apple->set_color('Red');

echo $apple->get_name();
echo $apple->get_color();