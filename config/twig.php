<?php

return array
(
	'environment' => array
	(
		'debug'               => FALSE,
		'trim_blocks'         => FALSE,
		'charset'             => 'utf-8',
		'base_template_class' => 'Twig_Template',
	),
	'extensions' => array
	(
		'Kohana_Twig_Extension_Trans',
		'Twig_Extension_Escaper',
	),
	'cache'          => APPPATH.'cache',
	'templates'      => APPPATH.'views',
	'auto_reload'    => TRUE,
	'suffix'         => '.twig',
	'context_object' => TRUE,
);