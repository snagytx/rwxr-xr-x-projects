<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.sopvid"
       name="Sopcast streams"
       version="VERSION_REPLACE"
       provider-name="rwxr_xr_x">
    <requires>
        <import addon="xbmc.python" version="1.0"/>
    </requires>
    <extension point="xbmc.python.pluginsource"
               library="default.py">
        <provides>video</provides>
    </extension>
    <extension point="xbmc.addon.metadata">
        <platform>linux</platform>
        <summary>Stream Sopcast channels.</summary>
        <description>Stream Sopcast channels.</description>
    </extension>
</addon>
