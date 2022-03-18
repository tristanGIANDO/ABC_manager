# Created by Tristan GIANDORIGGIO
# +33651839815
# giando.tristan@gmail.com

import maya.cmds as cmds
import os
import maya.mel as mel
       
suffix = "ANIM"

# CREATE EXPORT PATH
scene_name = cmds.file( q =1, sn = 1)
path_to_scene = os.path.dirname(scene_name)
path = os.path.join(path_to_scene)

# START FRAME END FRAME
start  = int(cmds.playbackOptions( q=True,min=True ))
end = int(cmds.playbackOptions( q=True,max=True ))
current = int(cmds.currentTime(q=True))

time_slider = str(int(start)) + ' ' + str(int(end))
current_frame = str(int(current)) + ' ' + str(int(current))

###### EXPORT AND BAKE CAMERA ########################################################################
def exportBakeCamera(*args):
    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query=1, text=1)
    sel = cmds.ls(sl=True)
    
    #REPATH TO CAMERA
    if "maya" in path:
        path_spl = path.split("maya")
        newpath = path_spl[0] + "camera"
        path2 = newpath.replace("\\", "/")    
    else:
        path2 = path.replace("\\", "/")
    
    #COMMAND
    for x in sel:
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            #EXPORT
            command = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + 'CAM_' + name + '.abc' + ' ";'
            mel.eval(command)
            mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "' + path2 + '/' + 'CAM_' + name + '.ma";')
            print ( " CAMERA is exported >> current frame ") 
        else:
            #BAKE
            for i in range(start,end):
                cmds.currentTime(i)
                cmds.setKeyframe(sel)
            #EXPORT
            command = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + 'CAM_' + name + '.abc' + ' ";'
            mel.eval(command)
            mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "' + path2 + '/' + 'CAM_' + name + '.ma";')
            print ( " CAMERA is exported >> Time Slider ")
       
###### EXPORT LINDSEY ########################################################################
def exportLindsey(*args):
    char_space = cmds.textField(lindsey_space_text, query = True, text = True)
    char_geo = "Lindsey_P_geoHi:Lindsey_MESH"
    char_head = "Lindsey_P_geoHi:Lindsey_head"

    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/") 
    else:
        path2 = path.replace("\\", "/")
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        abc_head = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
        for abc in [abc_geo, abc_head]:
            mel.eval(abc)
        print ( " I'm exporting the current frame ! ")
        print ( " Lindsey is exported >> MESH, HEAD")
        print ( " #FightForLindseyBlonde")
    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        abc_head = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
        for abc in [abc_geo, abc_head]:
            mel.eval(abc)
        print ( " I'm exporting the Time Slider ! ")
        print ( " Lindsey is exported >> MESH, HEAD")
        print ( " #FightForLindseyBlonde")

###### EXPORT BRUCE ########################################################################
def exportBruce(*args):
    char_space = cmds.textField(bruce_space_text, query = True, text = True)
    char_geo = "Bruce_P_geoHi:Bruce_MESH"
    char_head = "Bruce_P_geoHi:Bruce_head"
    char_arms = "Bruce_P_geoHi:Bruce_arms"
    char_light = "CTRL_Light"

    # QUERY FILE NAME
    #name = cmds.menuItem(abc_name_text, query = True, l = True)
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
    else:
        path2 = path.replace("\\", "/")
    
    # EXPORT ATTRIBUTES IN SHAPE
    attributes = ["light_intensity", "ConeAngle"]
    attr_of_the_light=""
    for each in attributes:
        attr_of_the_light += " -attr "+ each 
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        abc_head = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
        abc_arms = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2 + '/' + name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
        abc_light = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2 + '/' + name + '_' + char_space + '_LIGHT' + '.abc' + ' ";'
        for abc in [abc_geo, abc_head, abc_arms, abc_light]:
            mel.eval(abc)
        print ( " I'm exporting the current frame ! ")
        print ( " Bruce is exported >> MESH, HEAD, ARMS, LIGHT")

    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        abc_head = 'AbcExport -j "-frameRange ' + time_slider + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
        abc_arms = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2 + '/' + name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
        abc_light = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2 + '/' + name + '_' + char_space + '_LIGHT' + '.abc' + ' ";'
        for abc in [abc_geo, abc_head, abc_arms, abc_light]:
            mel.eval(abc)
        print ( " I'm exporting the Time Slider ! ")
        print ( " Bruce is exported >> MESH, HEAD, ARMS, LIGHT")

###### EXPORT WILLIS ########################################################################
def exportWillis(*args):
    char_space = cmds.textField(willis_space_text, query = True, text = True)
    char_geo = "Willis_P_geoHi:grp_willis"

    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")   
    else:
        path2 = path.replace("\\", "/")
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Current frame exported >> " + name + '_' + char_space + "_" + suffix + ".abc")
    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Time Slider exported >> " + name + '_' + char_space + "_" + suffix + ".abc")

###### EXPORT WILLIS ########################################################################
def exportTentacle(*args):
    char_space = cmds.textField(tent_space_text, query = True, text = True)
    char_geo = "tentacle_P_geoHi:grp_tentacle"

    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")   
    else:
        path2 = path.replace("\\", "/")
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Current frame exported >> " + name + '_' + char_space + "_" + suffix + ".abc")
    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Time Slider exported >> " + name + '_' + char_space + "_" + suffix + ".abc")

###### EXPORT AND BAKE CAMERA ########################################################################
def exportAnything(*args):
    # QUERY FILE NAME
    name = cmds.textField(any_space_text, query = True, text = True) 
    shot_name = cmds.textField(abc_name_text, query = True, text = True)      
    sel = cmds.ls(sl=True)
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")   
    else:
        path2 = path.replace("\\", "/")
    
    #COMMAND
    for x in sel:
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            #EXPORT CURRENT FRAME
            command = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + shot_name + '_' + name + '_' + suffix + '.abc' + ' ";'
            mel.eval(command)
            print ( "Current frame exported >> " + shot_name + "_" + name + "_" + suffix + ".abc")
        else:
            #EXPORT TIME SLIDER
            command = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + shot_name + '_' + name + '_' + suffix + '.abc' + ' ";'
            mel.eval(command)
            print ( "Time Slider exported >> " + shot_name + "_" + name + "_" + suffix + ".abc")

#############################
## USER INTERFACE SETTINGS ##
#############################

diUi = {}
diUi["lays"] = {}
diUi["ctrls"] = {}
diUi["window"] = {}

if cmds.window("giando", exists=True):
	cmds.deleteUI("giando")
window = diUi["window"]["main"]= cmds.window("giando", title="ABC_Exporter_0.2", widthHeight=(20, 20), sizeable=True, maximizeButton=False)

###### LAYERS HIERARCHY
diUi["lays"]["global"] = cmds.frameLayout(l="EXPORT", p=diUi["window"]["main"], bgc=(0.0,0.5,0.5), cll=True)
diUi["lays"]["exportButtons"] = cmds.rowColumnLayout(nc =2, columnWidth=[(1, 80), (2,200)], p=diUi["lays"]["global"])

###########################################################

###### EXPORT BUTTONS
cmds.setParent (diUi["lays"]["exportButtons"])

cmds.text( label= "SHOT NAME", fn = "boldLabelFont")
abc_name_text = cmds.textField(tx="030")
cmds.text( label= "  ")
current_frame_UI = cmds.checkBox( label = "Export Current Frame")
cmds.separator()
cmds.separator()
cmds.text( label= "NameSpace")
cmds.text( label= "Functions")

lindsey_space_text = cmds.textField(tx="CHAR01")
cmds.button ( label = "Export LINDSEY", backgroundColor=[0.0, 0.5, 0.5], c= exportLindsey )
bruce_space_text = cmds.textField(tx="CHAR02")
cmds.button ( label = "Export BRUCE", backgroundColor=[0.0, 0.4, 0.4], c= exportBruce )
willis_space_text = cmds.textField(tx="CHAR03")
cmds.button ( label = "Export WILLIS", backgroundColor=[0.0, 0.3, 0.3], c= exportWillis )
tent_space_text = cmds.textField(tx="TENT01")
cmds.button ( label = "Export TENTACLE", backgroundColor=[0.0, 0.2, 0.2], c= exportTentacle )
any_space_text = cmds.textField(tx="Any")
cmds.button ( label = "Export ANYTHING", backgroundColor=[0.0, 0.1, 0.1], c= exportAnything )
cmds.text( label= "Select cam if >>")
cmds.button ( label = "Export And Bake CAMERA", backgroundColor=[0.0, 0.0, 0.0], c= exportBakeCamera )

cmds.showWindow (diUi["window"]["main"])