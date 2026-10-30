<?php

if ( !defined( 'MEDIAWIKI' ) ) {
	exit;
}

$wgSitename = 'Dumpster Fire Lore';
$wgMetaNamespace = 'Dumpster_Fire_Lore';
$wgScriptPath = '';
$wgArticlePath = '/index.php?title=$1';
$wgServer = getenv( 'MEDIAWIKI_SERVER' ) ?: 'http://localhost:8082';
$wgResourceBasePath = $wgScriptPath;
$wgLogos = [
	'1x' => "$wgResourceBasePath/resources/assets/change-your-logo.svg",
	'icon' => "$wgResourceBasePath/resources/assets/change-your-logo.svg",
];

$wgEnableEmail = false;
$wgEnableUserEmail = false;
$wgDBtype = 'mysql';
$wgDBserver = 'mediawiki-db';
$wgDBname = 'mediawiki';
$wgDBuser = 'mediawiki';
$wgDBpassword = getenv( 'MEDIAWIKI_DB_PASSWORD' );
$wgDBprefix = '';
$wgDBssl = false;
$wgDBTableOptions = 'ENGINE=InnoDB, DEFAULT CHARSET=binary';

$wgMainCacheType = CACHE_NONE;
$wgMemCachedServers = [];
$wgEnableUploads = true;
$wgUseInstantCommons = false;
$wgPingback = false;
$wgLanguageCode = 'en';
$wgLocaltimezone = 'Europe/Berlin';

$wgSecretKey = getenv( 'MEDIAWIKI_SECRET_KEY' );
$wgAuthenticationTokenVersion = '1';
$wgUpgradeKey = getenv( 'MEDIAWIKI_UPGRADE_KEY' );

$wgDefaultSkin = 'vector-2022';
wfLoadSkin( 'Vector' );

// Das Wiki ist das Buch: Leser sehen die letzte freigegebene Revision.
// Neue Seiten bleiben bis zur ersten Freigabe leer.
wfLoadExtension( 'ApprovedRevs' );
$egApprovedRevsEnabledNamespaces = [
	NS_MAIN => true,
];
$egApprovedRevsBlankIfUnapproved = true;
$egApprovedRevsAutomaticApprovals = false;
$egApprovedRevsShowNotApprovedMessage = true;
$egApprovedRevsShowApproveLatest = true;

wfLoadExtension( 'LoreBridge' );
$wgLoreBridgeApiSecret = getenv( 'LOREBRIDGE_API_SECRET' ) ?: '';
$wgLoreBridgeAllowedServers = [ 'dumpster-fire' ];
$wgLoreBridgeTicketLifetime = 300;

$wgShowExceptionDetails = false;
$wgShowDBErrorBacktrace = false;
$wgShowSQLErrors = false;
