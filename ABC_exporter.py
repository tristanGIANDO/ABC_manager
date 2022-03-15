# Created by Tristan GIANDORIGGIO
# +33651839815
# giando.tristan@gmail.com


import maya.cmds as cmds
import os
import maya.mel as mel
from os import listdir
from os.path import isfile, join

shotList = ["010",
            "020_010",
            "030",
            "040",
            "050",
            "070",
            "075",
            "080",
            "085",
            "090",
            "100",
            "110"]
            
suffix = "ANIM"



###### EXPORT AND BAKE CAMERA ########################################################################
def exportBakeCamera(*args):
    # QUERY FILE PATH    
    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query=1, text=1)
    
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
        
    sel = cmds.ls(sl=True)
    
    
    #REPATH TO CAMERA
    if "maya" in path:
        path_spl = path.split("maya")
        newpath = path_spl[0] + "camera"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #COMMAND
    for x in sel:
        #BAKE
        for i in range(start,end):
            cmds.currentTime(i)
            cmds.setKeyframe(sel)
        #EXPORT
        command = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + name + '.abc' + ' ";'
        mel.eval(command)
        mel.eval('file -force -options "v=0;" -typ "mayaAscii" -pr -es "' + path2 + '/' + name + '.ma";')
        print ( command )
       
###### EXPORT LINDSEY ########################################################################
def exportLindsey(*args):
    
    char_space = cmds.textField(lindsey_space_text, query = True, text = True)
    char_geo = "Lindsey_P_geoHi:Lindsey_MESH"
    char_head = "Lindsey_P_geoHi:Lindsey_head"
    char_proxy = "Lindsey_P_geoHi:Lindsey_PROXY"

    # QUERY FILE PATH    
    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
    
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #EXPORT
    abc_geo = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
    abc_head = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
    mel.eval(abc_geo)
    mel.eval(abc_head)

###### EXPORT BRUCE ########################################################################
def exportBruce(*args):
    
    char_space = cmds.textField(bruce_space_text, query = True, text = True)
    char_geo = "Bruce_P_geoHi:Bruce_MESH"
    char_head = "Bruce_P_geoHi:Bruce_head"
    char_arms = "Bruce_P_geoHi:Bruce_arms"

    # QUERY FILE PATH    
    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    #name = cmds.menuItem(abc_name_text, query = True, l = True)
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
    
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #EXPORT
    abc_geo = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
    abc_head = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
    abc_arms = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2 + '/' + name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
    mel.eval(abc_geo)
    mel.eval(abc_head)
    mel.eval(abc_arms)

###### EXPORT WILLIS ########################################################################
def exportWillis(*args):
    
    char_space = cmds.textField(willis_space_text, query = True, text = True)
    char_geo = "Willis_P_geoHi:grp_willis"

    # QUERY FILE PATH    
    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    #name = cmds.menuItem(abc_name_text, query = True, l = True)
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
    
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #EXPORT
    abc_geo = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
    mel.eval(abc_geo)

###### EXPORT WILLIS ########################################################################
def exportTentacle(*args):
    
    char_space = cmds.textField(tent_space_text, query = True, text = True)
    char_geo = "tentacle_P_geoHi:grp_tentacle"

    # QUERY FILE PATH    
    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    #name = cmds.menuItem(abc_name_text, query = True, l = True)
    name = cmds.textField(abc_name_text, query = True, text = True)
    print (name)
    
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
    
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #EXPORT
    abc_geo = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
    mel.eval(abc_geo)

###### EXPORT AND BAKE CAMERA ########################################################################
def exportAnything(*args):
    # QUERY FILE PATH    

    scene_name = cmds.file( q =1, sn = 1)
    path_to_scene = os.path.dirname(scene_name)
    path = os.path.join(path_to_scene)
    # QUERY FILE NAME
    name = cmds.textField(any_space_text, query = True, text = True) 
    shot_name = cmds.textField(abc_name_text, query = True, text = True)   
    # START FRAME END FRAME
    start  = int(cmds.playbackOptions( q=True,min=True ))
    end = int(cmds.playbackOptions( q=True,max=True ))
        
    sel = cmds.ls(sl=True)
    
    
    #REPATH TO CAMERA
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")
        
    else:
        path2 = path.replace("\\", "/")
    
    geo = []
    
    #COMMAND
    for x in sel:
        #EXPORT
        command = 'AbcExport -j "-frameRange ' + str(int(start)) + ' ' + str(int(end)) + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + x + ' -file ' + path2 + '/' + shot_name + '_' + name + '_' + suffix + '.abc' + ' ";'
        mel.eval(command)

#############################
## USER INTERFACE SETTINGS ##
#############################

diUi = {}
diUi["lays"] = {}
diUi["ctrls"] = {}
diUi["window"] = {}

if cmds.window("giando", exists=True):
	cmds.deleteUI("giando")
window = diUi["window"]["main"]= cmds.window("giando", title="ABC_Exporter_0.1", widthHeight=(20, 20), sizeable=True, maximizeButton=False)

###### LAYERS HIERARCHY
diUi["lays"]["global"] = cmds.frameLayout(l="EXPORT", p=diUi["window"]["main"], bgc=(0.0,0.5,0.5), cll=True)
diUi["lays"]["exportButtons"] = cmds.rowColumnLayout(nc =2, columnWidth=[(1, 80), (2,200)], p=diUi["lays"]["global"])

###########################################################


###### EXPORT BUTTONS
cmds.setParent (diUi["lays"]["exportButtons"])

cmds.text( label= "SHOT NAME", fn = "boldLabelFont")
abc_name_text = cmds.textField(tx="030")
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

cmds.text( label= " ")
cmds.button ( label = "Export And Bake CAMERA", backgroundColor=[0.0, 0.0, 0.0], c= exportBakeCamera )




cmds.showWindow (diUi["window"]["main"])