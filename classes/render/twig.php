<?php defined('SYSPATH') OR die('No direct access allowed.');

/**
 * Twig loader.
 *
 * @package  kohana-module-smarty
 * @author   Oded Arbel <oded@geek.co.il>
 */
class Render_Twig extends Render {
	
	private static $twig = null;
	
	public static function render(array $vars=array(), array $globals=array(), $file=false, array $options=array()) {
		$token = Kohana::$profiling ? Profiler::start('twig', 'rendering ' . basename($file)) : false;
		
		if (!isset(self::$twig)) {
			// Setup the Twig loader environment
			self::$twig = Kohana_Twig::instance();
		}
		
		$file = self::getTemplatePath($file);
		$renderedVars = array();
		foreach ($vars as $name => $var)
			$renderedVars[$name] = ($var instanceof View) ? $var->render(null, $options) : $var; 
		
		$result = self::$twig->loadTemplate($file)->render(array_merge($globals, $renderedVars));
		
		$token ? Profiler::stop($token) : null;
		return $result;
	}
	
	/**
	 * Return a relative path under the Twig loader's configured paths
	 * @param string $filepath full path to the file as genearted by the templating view
	 * @return string relative path if the configured path is valid, otherwise an invalid path for debugging
	 */
	private static function getTemplatePath($filepath) {
		// make sure that file under the paths that we configured twig with
		foreach (Kohana_Twig::$loader->getPaths() as $path) {
			$realpath = realpath($path);
			if (!$realpath) // the specified path is invalid
				continue;
			if (strpos($filepath, $realpath) === 0);
				return substr($filepath, strlen($realpath)+strlen(DIRECTORY_SEPARATOR));
		}
		
		return "-invalid-{$filepath}";
	}

}
