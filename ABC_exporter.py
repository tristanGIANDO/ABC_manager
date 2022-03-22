# Created by Tristan GIANDORIGGIO
# +33651839815
# giando.tristan@gmail.com

import maya.cmds as cmds
import os
import maya.mel as mel
       
suffix = "ANIM"
bruce = "Bruce"
lindsey = "Lindsey"
willis = "Willis"
willis_red = "WillisRed"
bruce_lookdev = os.path.join("bruce_P_lookdev.ma")
bruce_out_lookdev = os.path.join("bruce_OUT_P_lookdev.ma")
lindsey_lookdev = os.path.join("Lindsey_P_lookdev.ma")
willis_lookdev = os.path.join("Willis_P_lookdev.ma")
willis_red_lookdev = os.path.join("WillisRed_P_lookdev.ma")

# CREATE EXPORT PATH
scene_name = cmds.file( q =1, sn = 1)
print (scene_name)
path_to_scene = os.path.dirname(scene_name)
path = os.path.join(path_to_scene)

# START FRAME END FRAME
start  = int(cmds.playbackOptions( q=True,min=True ))
end = int(cmds.playbackOptions( q=True,max=True ))
current = int(cmds.currentTime(q=True))

time_slider = str(int(start)) + ' ' + str(int(end))
current_frame = str(int(current)) + ' ' + str(int(current))

# PATH TO LOOKDEV
server = os.path.join(r"\\gandalf/3D4_21_22",
                        "instinct",
                        )

char_path = os.path.join("04_asset",
                        "character")

shot_path = os.path.join("05_shot") 

shot_020_path = os.path.join("05_shot",
                        "seq0020")

scenes_path = os.path.join("maya",
                        "scenes",
                        "publish",
                        "lookdev")

cache_path = os.path.join("maya",
                        "cache")
                  

shot_list = ["010",
            "020_010",
            "020_020",
            "020_030",
            "020_040",
            "020_050",
            "020_055",
            "020_060",
            "020_080",
            "020_090",
            "020_100",
            "020_110",
            "020_120",
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

bruce_lookdev_path = os.path.join( server,
                        bruce_lookdev)

bruce_OUT_lookdev_path = os.path.join( server,
                        char_path,
                        bruce,
                        scenes_path,
                        bruce_out_lookdev)

lindsey_lookdev_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_lookdev)

willis_lookdev_path = os.path.join( server,
                        char_path,
                        willis,
                        scenes_path,
                        willis_lookdev)

willis_red_lookdev_path = os.path.join( server,
                        char_path,
                        willis_red,
                        scenes_path,
                        willis_red_lookdev)

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
    char_space = "CHAR01"
    char_geo = "Lindsey_P_geoHi:Lindsey_MESH"
    char_head = "Lindsey_P_geoHi:Lindsey_head"

    
    # QUERY FILE NAME
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 

    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name
        path2 = newpath.replace("\\", "/")
        anim = os.path.join(shot_name + "_" + char_space + "_" + suffix + ".abc")

        #EXPORT
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
            abc_head = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
            for abc in [abc_geo, abc_head]:
                mel.eval(abc)
            print ( " I'm exporting the current frame ! ")
            print ( " Lindsey is exported >> MESH, HEAD")
            print ( " #FightForLindseyBlonde")
        else:
            abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
            abc_head = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
            for abc in [abc_geo, abc_head]:
                mel.eval(abc)
            print ( " I'm exporting the Time Slider ! ")
            print ( " Lindsey is exported >> MESH, HEAD")
            print ( " #FightForLindseyBlonde")

###### EXPORT BRUCE ########################################################################
def exportBruce(*args):
    char_space = "CHAR02"
    char_geo = "Bruce_P_geoHi:Bruce_MESH"
    char_head = "Bruce_P_geoHi:Bruce_head"
    char_arms = "Bruce_P_geoHi:Bruce_arms"
    char_mask = "Bruce_P_geoHi:Bruce_arms" #####################################
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
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
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
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("scenes")
        newpath = path_spl[0] + "cache"
        path2 = newpath.replace("\\", "/")   
    else:
        path2 = path.replace("\\", "/")

    # if ".ma" in scene_name:
    #     print ( "yo" )
    #     split = path.split("_A_*")
    #     print ( split )
    
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

def export_char(*args):
    exportLindsey()

###### IMPORT AND MERGE ABC ###############################################################################
def import_abc(*args):
    
    character = cmds.optionMenu (import_menu, q=True, v=True)
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 
    abc_Lindsey = str(shot_name + "_CHAR01_ANIM.abc")
    abc_Bruce = str(shot_name + "_CHAR02_ANIM.abc")
    abc_Willis = str(shot_name + "_CHAR03_ANIM.abc")
    abc_Bruce_light = str(shot_name + "_CHAR02_LIGHT.abc")

    path = os.path.join(server,
                        shot_path,
                        shot_name,
                        cache_path)

    path_020 = os.path.join(server,
                        shot_020_path,
                        shot_name,
                        cache_path)
    
    if "LINDSEY" in character:
        path_to_lindsey = os.path.join(path,
                        abc_Lindsey)
        path_to_lindsey_020 = os.path.join(path_020,
                        abc_Lindsey)


        cmds.file(lindsey_lookdev_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev

        if "020_" in path_to_lindsey:
            cmds.AbcImport(str(path_to_lindsey_020), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
            print ( "Pray for Lindsey Blonde")
        else:
            cmds.AbcImport(str(path_to_lindsey), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
            print ( "Pray for Lindsey Blonde")

    if "BRUCE" in character:
        path_to_bruce = os.path.join(path,
                        abc_Bruce)
        path_to_light = os.path.join(path,
                        abc_Bruce_light)
        path_to_bruce_020 = os.path.join(path_020,
                        abc_Bruce)
        path_to_light_020 = os.path.join(path_020,
                        abc_Bruce_light)

        cmds.file(bruce_OUT_lookdev_path, r=True, ignoreVersion = True, namespace = "CHAR02") # Reference Bruce Lookdev

        if "020_" in path_to_bruce:
            cmds.AbcImport(str(path_to_bruce_020), mode='import', connect= "CHAR02:Bruce_P_geoHi:Bruce_MESH") # Merge ABC
            cmds.AbcImport(str(path_to_light_020), mode='import') #Import CTRL Light

        else :
            cmds.AbcImport(str(path_to_bruce), mode='import', connect= "CHAR02:Bruce_P_geoHi:Bruce_MESH") # Merge ABC
            cmds.AbcImport(str(path_to_light), mode='import') #Import CTRL Light
        
        try:
            disk_light = cmds.shadingNode("PxrDiskLight", asLight=True, n= "TORCHE_light") #Create Light
            cmds.matchTransform(disk_light,"CHAR02:CTRL_Light")
            cmds.parent(disk_light, "CHAR02:CTRL_Light")

            cmds.connectAttr("CHAR02:Bruce_P_geoHi:Bruce_headShape.light_intensity" ,"TORCHE_light.intensity") # Connect intensity
            cmds.connectAttr("CHAR02:Bruce_P_geoHi:Bruce_headShape.ConeAngle" ,"TORCHE_light.coneAngle") # Connect intensity

            print ( "done" )
        except:
            print (" no light" )

    if "WHITE" in character:
        path_to_willis = os.path.join(path,
                        abc_Willis)
        try :
            cmds.file(willis_lookdev_path, r=True, ignoreVersion = True, namespace = "CHAR03") # Reference Willis Lookdev
            cmds.AbcImport(str(path_to_willis), mode='import', connect= "CHAR03:Willis_P_geoHi:grp_willis") # Merge ABC
            print ( "Fais danser ta blanche ventouse Willis")
        except :
            print ("no no no no")

    if "RED" in character:
        path_to_willis = os.path.join(path,
                        abc_Willis)
        try :
            cmds.file(willis_red_lookdev_path, r=True, ignoreVersion = True, namespace = "CHAR03") # Reference Willis Lookdev
            cmds.AbcImport(str(path_to_willis), mode='import', connect= "CHAR03:Willis_P_geoHi:grp_willis") # Merge ABC
            print ( "Fais vriller ta rouge ventouse Willis")
        except :
            print ("no no no no")

    else:
        path2 = path.replace("\\", "/")

def import_cam(*args):
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True)
    # shot_name = cmds.textField(merge_shot_UI, query = True, text = True)
    abc_camera = str( "CAM_" + shot_name + ".abc")
    path = os.path.join(server,
                        shot_path,
                        shot_name,
                        "camera",
                        abc_camera)

    path_020 = os.path.join(server,
                        shot_020_path,
                        shot_name,
                        "camera",
                        abc_camera)

    try:
        cmds.file(path, i = True) #Import cam
    except:
        try:
            cmds.file(path_020, i = True) #Import cam
        except:
            print ( "oww, no cam")


#############################
## USER INTERFACE SETTINGS ##
#############################

diUi = {}
diUi["lays"] = {}
diUi["ctrls"] = {}
diUi["window"] = {}

if cmds.window("giando", exists=True):
	cmds.deleteUI("giando")
window = diUi["window"]["main"]= cmds.window("giando", title="ABC_Manager_0.3", widthHeight=(20, 20), sizeable=True, maximizeButton=False)

###### LAYERS HIERARCHY
diUi["lays"]["manager"] = cmds.frameLayout("GLOBAL", p=diUi["window"]["main"], bgc=(0.0,0.0,0.0))
diUi["lays"]["shot"] = cmds.columnLayout(adj = True, p=diUi["lays"]["manager"])
# TAB EXPORT
diUi["lays"]["e_global"] = cmds.frameLayout("EXPORT", p=diUi["window"]["main"], bgc=(0.0,0.0,0.0), cll =True)
diUi["lays"]["exportButtons"] = cmds.rowColumnLayout(nc =2, columnWidth=[(1, 170), (2,80)], p=diUi["lays"]["e_global"])
diUi["lays"]["text"] = cmds.columnLayout(adj = True, p=diUi["lays"]["e_global"])
diUi["lays"]["cam"] = cmds.rowColumnLayout(nc =2, columnWidth=[(1, 90), (2,150)], p=diUi["lays"]["e_global"])
# TAB IMPORT
diUi["lays"]["i_global"] = cmds.frameLayout("IMPORT", p=diUi["window"]["main"], bgc=(0.0,0.0,0.0), cll = True)
diUi["lays"]["import"] = cmds.columnLayout(adj = True, p=diUi["lays"]["i_global"])

###########################################################
cmds.setParent (diUi["lays"]["shot"])
choose_shot = cmds.optionMenu( label= "Select Shot" )
for shot in shot_list:
    a = cmds.menuItem(shot)

import_menu = cmds.optionMenu( label= "Select Character" )
# ITEMS
lindsey_lookdev_UI = cmds.menuItem( label= "LINDSEY" )
bruce_out_lookdev_UI = cmds.menuItem( label= "BRUCE_OUT" )
willis_lookdev_UI = cmds.menuItem( label= "WILLIS WHITE" )
willis_red_lookdev_UI = cmds.menuItem( label= "WILLIS RED" )

###### EXPORT BUTTONS
cmds.setParent (diUi["lays"]["exportButtons"])
tent_space_text = cmds.text(label = "Namespace if TENTACLE")
tent_space_text = cmds.textField(tx="TENT01")
any_space_text = cmds.text(label = "Namespace if CUSTOM")
any_space_text = cmds.textField(tx="CUSTOM")
cmds.text( label= "  ")


###### TEXT
cmds.setParent (diUi["lays"]["text"])
current_frame_UI = cmds.checkBox( label = "Export Current Frame")
cmds.button ( label = "Export CHARACTER", backgroundColor=[0.0, 0.6, 0.6], c= export_char )
cmds.button ( label = "Export TENTACLE", backgroundColor=[0.0, 0.5, 0.5], c= exportTentacle )
cmds.button ( label = "Export CUSTOM", backgroundColor=[0.0, 0.4, 0.4], c= exportAnything )

cmds.setParent (diUi["lays"]["cam"])
cmds.text( label= "Select cam if >> ")
cmds.button ( label = "Export And Bake CAMERA", backgroundColor=[0.0, 0.3, 0.3], c= exportBakeCamera )

#############################################################
cmds.setParent (diUi["lays"]["import"])
# BUTTONS
cmds.button ( label = "Import and Merge ABC", backgroundColor=[0.0, 0.2, 0.2], c= import_abc)
cmds.button ( label = "Import Camera", backgroundColor=[0.0, 0.1, 0.1], c= import_cam)

cmds.showWindow (diUi["window"]["main"])