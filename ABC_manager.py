
# Created by Tristan GIANDORIGGIO
# +33651839815
# giando.tristan@gmail.com

title = "ABC Manager "
version = "1.0.1"

import maya.cmds as cmds
import os
import maya.mel as mel
       




suffix = "ANIM"
bruce = "Bruce"
lindsey = "Lindsey"
willis = "Willis"
willis_red = "WillisRed"
zodiac = "zodiac"
bruce_lookdev = os.path.join("bruce_P_lookdev.ma")
bruce_out_lookdev = os.path.join("bruce_OUT_P_lookdev.ma")
lindsey_20 = os.path.join("Lindsey_P_lookdev.ma")
lindsey_40 = os.path.join("040_Lindsey_P_lookdev.ma")
lindsey_30_50_70 = os.path.join("Lindsey_IN_01_P_lookdev.ma")
lindsey_70_to_90 = os.path.join("Lindsey_IN_02_P_lookdev.ma")
lindsey_90_to_110 = os.path.join("Lindsey_IN_03_P_lookdev.ma")
willis_lookdev = os.path.join("Willis_P_lookdev.ma")
willis_red_lookdev = os.path.join("WillisRed_P_lookdev.ma")
zodiac_lookdev = os.path.join("zodiac_P_lookdev.ma")

shot_list = ["010",
            "020_007",
            "020_010",
            "020_020",
            "020_030",
            "020_040",
            "020_050",
            "020_055",
            "020_060",
            "020_080",
            "020_100",
            "020_110",
            "020_120",
            "030",
            "sh0040",
            "050",
            "070",
            "075",
            "080",
            "085",
            "090",
            "100",
            "110"]

# CREATE EXPORT PATH
scene_name = cmds.file( q =1, sn = 1)
print (scene_name)
path_to_scene = os.path.dirname(scene_name)
path = os.path.join(path_to_scene)

# START FRAME END FRAME
# start  = int(cmds.playbackOptions( q=True,min=True ))
start  = int(950)
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

prop_path = os.path.join("04_asset",
                        "prop")

shot_path = os.path.join("05_shot") 

shot_020_path = os.path.join("05_shot",
                        "seq0020")

scenes_path = os.path.join("maya",
                        "scenes",
                        "publish",
                        "lookdev")

cache_path = os.path.join("maya",
                        "cache")
                  




bruce_OUT_lookdev_path = os.path.join( server,
                        char_path,
                        bruce,
                        scenes_path,
                        bruce_out_lookdev)

lindsey_lookdev_20_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_20)

lindsey_lookdev_40_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_40)

lindsey_lookdev_50_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_30_50_70)

lindsey_lookdev_70_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_70_to_90)

lindsey_lookdev_90_path = os.path.join( server,
                        char_path,
                        lindsey,
                        scenes_path,
                        lindsey_90_to_110)

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

zodiac_lookdev_path = os.path.join( server,
                        prop_path,
                        zodiac,
                        scenes_path,
                        zodiac_lookdev)

###### EXPORT AND BAKE CAMERA ########################################################################
def exportBakeCamera(*args):
    # QUERY FILE NAME
    name = cmds.optionMenu (choose_shot, q=True, v=True) 

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))

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
            # for i in range(start,end):
            #     cmds.currentTime(i)
            #     cmds.setKeyframe(sel)
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
    char_collider = "COLLIDER"
    char_cloth = "Combi_LOW"
    char_braid = "crv_tresse_hair_rebuilt"

    
    # QUERY FILE NAME
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))


    #REPATH TO CACHE
    if "scenes" in path:
        #classic path
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name
        path2 = newpath.replace("\\", "/")

        #path 020
        path_spl_020 = path.split("05_shot")
        newpath_020 = path_spl_020[0] + "05_shot/seq0020/" + shot_name
        path2_020 = newpath_020.replace("\\", "/")

        anim = os.path.join(shot_name + "_" + char_space + "_" + suffix + ".abc") #Nom du fichier à exporter

        print (path)


        #EXPORT
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            if "seq0020" in path:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
               
                #export groom
                if cmds.checkBox(check_L_groom, q = True, v = True):
                    abc_head = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    abc_braid = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_braid + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_BRAID' + '.abc' + ' ";'
                    mel.eval(abc_braid)
                
                #export cloth
                if cmds.checkBox(check_L_cloth, q = True, v = True):
                    abc_collider = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_collider + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_COLLIDER' + '.abc' + ' ";'
                    abc_cloth = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_cloth + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_CLOTH' + '.abc' + ' ";'
                    mel.eval(abc_collider)
                    mel.eval(abc_cloth)
              
                print ( " I'm exporting the current frame ! ")
                print ( " #FightForLindseyBlonde")
            else:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
               
                #export groom
                if cmds.checkBox(check_L_groom, q = True, v = True):
                    abc_head = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    abc_braid = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_braid + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_BRAID' + '.abc' + ' ";'
                    mel.eval(abc_braid)

                #export cloth
                if cmds.checkBox(check_L_cloth, q = True, v = True):
                    abc_collider = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_collider + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_COLLIDER' + '.abc' + ' ";'
                    abc_cloth = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_cloth + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_CLOTH' + '.abc' + ' ";'
                    mel.eval(abc_collider)
                    mel.eval(abc_cloth)

                print ( " I'm exporting the current frame ! ")
                print ( " #FightForLindseyBlonde")

        else:
            if "seq0020" in path:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
               
                #export groom
                if cmds.checkBox(check_L_groom, q = True, v = True):
                    abc_head = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    abc_braid = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_braid + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_BRAID' + '.abc' + ' ";'
                    mel.eval(abc_braid)

                #export cloth
                if cmds.checkBox(check_L_cloth, q = True, v = True):
                    abc_collider = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_collider + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_COLLIDER' + '.abc' + ' ";'
                    abc_cloth = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_cloth + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_CLOTH' + '.abc' + ' ";'
                    mel.eval(abc_collider)
                    mel.eval(abc_cloth)

                print ( " I'm exporting the Time Slider ! ")
                
                print ( " #FightForLindseyBlonde")
            else:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
               
                #export groom
                if cmds.checkBox(check_L_groom, q = True, v = True):
                    abc_head = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    abc_braid = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_braid + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_BRAID' + '.abc' + ' ";'
                    mel.eval(abc_braid)

                #export cloth
                if cmds.checkBox(check_L_cloth, q = True, v = True):
                    abc_collider = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_collider + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_COLLIDER' + '.abc' + ' ";'
                    abc_cloth = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_cloth + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_CLOTH' + '.abc' + ' ";'
                    mel.eval(abc_collider)
                    mel.eval(abc_cloth)

                print ( " I'm exporting the Time Slider ! ")
                print ( " #FightForLindseyBlonde")

###### EXPORT BRUCE ########################################################################
def exportBruce(*args):
    char_space = "CHAR02"
    char_geo = "Bruce_P_geoHi:Bruce_MESH"
    char_head = "Bruce_P_geoHi:Bruce_head"
    char_arms = "Bruce_P_geoHi:Bruce_arms"
    char_mask = "Bruce_P_geoHi:Grp_mask" #####################################
    char_light = "CTRL_Light"
    char_emitter = "emitter_geo"

    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name
        path2 = newpath.replace("\\", "/")

        #path 020
        path_spl_020 = path.split("05_shot")
        newpath_020 = path_spl_020[0] + "05_shot/seq0020/" + shot_name
        path2_020 = newpath_020.replace("\\", "/")

        print (path + "")
    
        # EXPORT ATTRIBUTES IN SHAPE
        attributes = ["light_intensity", "ConeAngle"]
        attr_of_the_light=""
        for each in attributes:
            attr_of_the_light += " -attr "+ each 
        
        #EXPORT
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            if "seq0020" in path: #Exporter seq020
                if cmds.checkBox(check_B_geo, q = True, v = True): #export geo
                    abc_geo = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
                    mel.eval(abc_geo)
                if cmds.checkBox(check_B_groom, q = True, v = True): #export head + arms
                    abc_head = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    abc_arms = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    mel.eval(abc_arms)
                if cmds.checkBox(check_B_light, q = True, v = True): # export light
                    abc_light = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_LIGHT' + '.abc' + ' ";'
                    mel.eval(abc_light)
                if cmds.checkBox(check_B_mask, q = True, v = True): # export mask
                    abc_mask = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_mask + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_MASK' + '.abc' + ' ";'
                    mel.eval(abc_mask)
                if cmds.checkBox(check_B_emitter, q = True, v = True): # export emitter
                    abc_emit = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_emitter + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_EMIT' + '.abc' + ' ";'
                    mel.eval(abc_emit)
                print ( "I'm exporting the current frame ! ")
            
            else: #Exporter classic seq
                if cmds.checkBox(check_B_geo, q = True, v = True): #export geo
                    abc_geo = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
                    mel.eval(abc_geo)
                if cmds.checkBox(check_B_groom, q = True, v = True): #export head + arms
                    abc_head = 'AbcExport -j "-frameRange ' + current_frame + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    abc_arms = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    mel.eval(abc_arms)
                if cmds.checkBox(check_B_light, q = True, v = True): # export light
                    abc_light = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_LIGHT' + '.abc' + ' ";'
                    mel.eval(abc_light)
                if cmds.checkBox(check_B_mask, q = True, v = True): # export mask
                    abc_mask = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_mask + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_MASK' + '.abc' + ' ";'
                    mel.eval(abc_mask)
                if cmds.checkBox(check_B_emitter, q = True, v = True): # export emitter
                    abc_emit = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_emitter + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_EMIT' + '.abc' + ' ";'
                    mel.eval(abc_emit)
                print ( "I'm exporting the current frame ! ")

        else: #timeslider
            if "seq0020" in path: #Exporter seq020
                if cmds.checkBox(check_B_geo, q = True, v = True): #export geo
                    abc_geo = 'AbcExport -j "-frameRange ' + time_slider + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
                    mel.eval(abc_geo)
                if cmds.checkBox(check_B_groom, q = True, v = True): #export head + arms
                    abc_head = 'AbcExport -j "-frameRange ' + time_slider + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    abc_arms = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    mel.eval(abc_arms)
                if cmds.checkBox(check_B_light, q = True, v = True): # export light
                    abc_light = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_LIGHT' + '.abc' + ' ";'
                    mel.eval(abc_light)
                if cmds.checkBox(check_B_mask, q = True, v = True): # export mask
                    abc_mask = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_mask + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_MASK' + '.abc' + ' ";'
                    mel.eval(abc_mask)
                if cmds.checkBox(check_B_emitter, q = True, v = True): # export emitter
                    abc_emit = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_emitter + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_EMIT' + '.abc' + ' ";'
                    mel.eval(abc_emit)
                print ( "I'm exporting the time slider ! ")
            else:
                if cmds.checkBox(check_B_geo, q = True, v = True): #export geo
                    abc_geo = 'AbcExport -j "-frameRange ' + time_slider + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
                    mel.eval(abc_geo)
                if cmds.checkBox(check_B_groom, q = True, v = True): #export head + arms
                    abc_head = 'AbcExport -j "-frameRange ' + time_slider + attr_of_the_light + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_head + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_HEAD' + '.abc' + ' ";'
                    abc_arms = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_arms + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_ARMS' + '.abc' + ' ";'
                    mel.eval(abc_head)
                    mel.eval(abc_arms)
                if cmds.checkBox(check_B_light, q = True, v = True): # export light
                    abc_light = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_light + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_LIGHT' + '.abc' + ' ";'
                    mel.eval(abc_light)
                if cmds.checkBox(check_B_mask, q = True, v = True): # export mask
                    abc_mask = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_mask + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_MASK' + '.abc' + ' ";'
                    mel.eval(abc_mask)
                if cmds.checkBox(check_B_emitter, q = True, v = True): # export emitter
                    abc_emit = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_emitter + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space  + '_EMIT' + '.abc' + ' ";'
                    mel.eval(abc_emit)
                print ( "I'm exporting the time slider ! ")

###### EXPORT WILLIS ########################################################################
def exportWillis(*args):
    char_space = "CHAR03"
    char_geo = "Willis_P_geoHi:grp_willis"
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))
    
    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name
        path2 = newpath.replace("\\", "/")
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Willis is exported >> MESH")
    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Willis is exported >> MESH")

###### EXPORT WILLIS ########################################################################
def exportTentacle(*args):
    char_space = cmds.textField(tent_space_text, query = True, text = True)
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 
    char_geo = "tentacle_P_geoHi:grp_tentacle"

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))

    #REPATH TO CACHE
    if "scenes" in path:
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name
        path2 = newpath.replace("\\", "/")
  
    
    #EXPORT
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Current frame exported >> " + shot_name + '_' + char_space + "_" + suffix + ".abc")
    else:
        abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2 + '/' + 'maya' + '/' + 'cache' + '/' + shot_name + '_' + char_space + '_' + suffix + '.abc' + ' ";'
        mel.eval(abc_geo)
        print ( "Time Slider exported >> " + shot_name + '_' + char_space + "_" + suffix + ".abc")

###### EXPORT ZODIAC ########################################################################
def exportZodiac(*args):
    char_space = "ZODIAC"
    char_geo = "zodiac_P_geoHi:ZODIAC_mesh"

    # QUERY FILE NAME
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))


    #REPATH TO CACHE
    if "scenes" in path:
        #classic path
        path_spl = path.split("05_shot")
        newpath = path_spl[0] + "05_shot/" + shot_name

        #path 020
        path_spl_020 = path.split("05_shot")
        newpath_020 = path_spl_020[0] + "05_shot/seq0020/" + shot_name
        path2_020 = newpath_020.replace("\\", "/")

        anim = os.path.join(shot_name + "_" + char_space + "_" + suffix + ".abc") #Nom du fichier à exporter

        print (path)


        #EXPORT
        if cmds.checkBox(current_frame_UI, q = True, v = True):
            if "seq0020" in path:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + current_frame + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
                    print ( " I'm exporting the current frame ! ")
            else:
                print ( "Not SEQ020")
        else:
            if "seq0020" in path:
                #export geo
                if cmds.checkBox(check_L_geo, q = True, v = True):
                    abc_geo = 'AbcExport -j "-frameRange ' + time_slider + ' -uvWrite -worldSpace -writeVisibility -writeUVSets -dataFormat ogawa -root ' + char_space + ':' + char_geo + ' -file ' + path2_020 + '/' + 'maya' + '/' + 'cache' + '/' + anim + ' ";'
                    mel.eval(abc_geo)
                    print ( " I'm exporting the current frame ! ")
            else:
                print ( "Not SEQ020")

###### EXPORT AND BAKE CAMERA ########################################################################
def exportAnything(*args):
    # QUERY FILE NAME
    name = cmds.textField(any_space_text, query = True, text = True) 
    shot_name = cmds.textField(abc_name_text, query = True, text = True)   

    start = cmds.textField(start_frame_UI, query = True, text = True)
    end = cmds.textField(end_frame_UI, query = True, text = True)
    time_slider = str(int(start)) + ' ' + str(int(end))

    sel = cmds.ls(sl=True)
    
    #REPATH TO CACHE
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

def export_char(*args):
    character = cmds.optionMenu (import_menu, q=True, v=True)

    if cmds.checkBox(all_UI, q = True, v = True):
        try:
            exportLindsey()
        except:
            print ( "No Lindsey, no chocolat")
        try:
            exportBruce()
        except:
            print ( "No Bruce, no bus")
        try:
            exportWillis()
        except:
            print ( "No Willis, no police")
        try:
            exportZodiac()
        except:
            print ( "No Zodiac, nymphomaniac")

    else:  
        if "LINDSEY" in character:
            exportLindsey()
        
        if "BRUCE" in character:
            exportBruce()

        if "WILLIS" in character:    
            exportWillis()

        if "TENTACLE" in character:    
            exportTentacle()

        if "ZODIAC" in character:    
            exportZodiac()

###### IMPORT AND MERGE ABC ###############################################################################
def import_abc(*args):
    
    character = cmds.optionMenu (import_menu, q=True, v=True)
    shot_name = cmds.optionMenu (choose_shot, q=True, v=True) 
    abc_Lindsey = str(shot_name + "_CHAR01_ANIM.abc")
    abc_Bruce = str(shot_name + "_CHAR02_ANIM.abc")
    abc_Willis = str(shot_name + "_CHAR03_ANIM.abc")
    abc_Bruce_light = str(shot_name + "_CHAR02_LIGHT.abc")
    abc_Zodiac = str(shot_name + "_ZODIAC_ANIM.abc")
    # path to classic shots
    path = os.path.join(server,
                        shot_path,
                        shot_name,
                        cache_path)
    # path to seq 020
    path_020 = os.path.join(server,
                        shot_020_path,
                        shot_name,
                        cache_path)
    
    
    if "20" in character:
        path_to_lindsey_020 = os.path.join(path_020,
                        abc_Lindsey)

        cmds.file(lindsey_lookdev_20_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev
        cmds.AbcImport(str(path_to_lindsey_020), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
        print ( "Pray for Lindsey Blonde")


    if "40" in character:
        path_to_lindsey = os.path.join(path,
                        abc_Lindsey)

        cmds.file(lindsey_lookdev_40_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev
        cmds.AbcImport(str(path_to_lindsey), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
        print ( "Pray for Lindsey Blonde")

    if "50" in character:
        path_to_lindsey = os.path.join(path,
                        abc_Lindsey)

        cmds.file(lindsey_lookdev_50_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev
        cmds.AbcImport(str(path_to_lindsey), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
        print ( "Pray for Lindsey Blonde")

    if "75" in character:
        path_to_lindsey = os.path.join(path,
                        abc_Lindsey)

        cmds.file(lindsey_lookdev_70_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev
        cmds.AbcImport(str(path_to_lindsey), mode='import', connect= "CHAR01:Lindsey_P_geoHi:Lindsey_MESH") # Merge ABC
        print ( "Pray for Lindsey Blonde")

    if "100" in character:
        path_to_lindsey = os.path.join(path,
                        abc_Lindsey)

        cmds.file(lindsey_lookdev_90_path, r=True, ignoreVersion = True, namespace = "CHAR01") # Reference Lindsey Lookdev
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

    if "ZODIAC" in character:
        path_to_zodiac_020 = os.path.join(path_020,
                        abc_Zodiac)


        cmds.file(zodiac_lookdev_path, r=True, ignoreVersion = True, namespace = "ZODIAC") # Reference Lindsey Lookdev
        cmds.AbcImport(str(path_to_zodiac_020), mode='import', connect= "ZODIAC:zodiac_P_geoHi:ZODIAC_mesh") # Merge ABC
        print ( "Le zodiac explose")

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

def change_vis_checkbox(*args):
    if cmds.checkBox(all_UI, q = True, v = True):
        cmds.optionMenu(import_menu, edit = True, en = False)
        for lindsey in [check_L_geo, check_L_cloth, check_L_groom]:
            cmds.checkBox(lindsey, edit = True, en = True)
        for bruce in [check_B_geo, check_B_light, check_B_groom, check_B_mask, check_B_emitter]:
            cmds.checkBox(bruce, edit = True, en = True)
    else:
        cmds.optionMenu(import_menu, edit = True, en = True)
        for lindsey in [check_L_geo, check_L_cloth, check_L_groom]:
            cmds.checkBox(lindsey, edit = True, en = False)
        for bruce in [check_B_geo, check_B_light, check_B_groom, check_B_mask, check_B_emitter]:
            cmds.checkBox(bruce, edit = True, en = False)

def change_vis_menu(*args):
    character = cmds.optionMenu (import_menu, q=True, v=True)
    if "TENTACLE" in character:
        cmds.textField(tent_space_text, edit = True, en = True)
        cmds.text(tent_space_lbl, edit = True, en = True)
    else:
        cmds.textField(tent_space_text, edit = True, en = False)
        cmds.text(tent_space_lbl, edit = True, en = False)
    
    if "LINDSEY" in character:
        for lindsey in [check_L_geo, check_L_cloth, check_L_groom]:
            cmds.checkBox(lindsey, edit = True, en = True)
    else:
        for lindsey in [check_L_geo, check_L_cloth, check_L_groom]:
            cmds.checkBox(lindsey, edit = True, en = False)

    if "BRUCE" in character:
        for bruce in [check_B_geo, check_B_light, check_B_groom, check_B_mask, check_B_emitter]:
            cmds.checkBox(bruce, edit = True, en = True)    
    else:
        for bruce in [check_B_geo, check_B_light, check_B_groom, check_B_mask, check_B_emitter]:
            cmds.checkBox(bruce, edit = True, en = False)

def change_vis_frame_range(*args):
    if cmds.checkBox(current_frame_UI, q = True, v = True):
        cmds.textField(start_frame_UI, edit = True, en = False)
        cmds.textField(end_frame_UI, edit = True, en = False)
    else:
        cmds.textField(start_frame_UI, edit = True, backgroundColor=[1.0, 1.0, 1.0], en = True)
        cmds.textField(end_frame_UI, edit = True, backgroundColor=[1.0, 1.0, 1.0], en = True)

#############################
## USER INTERFACE SETTINGS ##
#############################

diUi = {}
diUi["lays"] = {}
diUi["ctrls"] = {}
diUi["window"] = {}

if cmds.window("giando", exists=True):
	cmds.deleteUI("giando")
window = diUi["window"]["main"]= cmds.window("giando", title= title + version, widthHeight=(20, 20), sizeable=True, maximizeButton=False)

###### LAYERS HIERARCHY
diUi["lays"]["manager"] = cmds.frameLayout("GLOBAL", p=diUi["window"]["main"], bgc=(0.0,0.0,0.0))
diUi["lays"]["shot"] = cmds.columnLayout(adj = True, p=diUi["lays"]["manager"])
# TAB EXPORT



tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, p=diUi["window"]["main"], bgc=(0.6,0.6,0.6), bs = "full")

diUi["lays"]["exportButtons"] = cmds.rowColumnLayout(numberOfColumns=2)
cmds.setParent( '..' )


# diUi["lays"]["import"] = cmds.rowColumnLayout(numberOfColumns=2)
diUi["lays"]["import"] = cmds.columnLayout(adj=True)
cmds.setParent( '..' )

cmds.tabLayout( tabs, edit=True, tabLabel=((diUi["lays"]["exportButtons"], 'EXPORT'), (diUi["lays"]["import"], 'IMPORT')) )

###########################################################
cmds.setParent (diUi["lays"]["shot"])
choose_shot = cmds.optionMenu( label= "Select Shot" )
for shot in shot_list:
    a = cmds.menuItem(shot)

import_menu = cmds.optionMenu( label= "Select Character" , cc = change_vis_menu)
# ITEMS
lindsey_lookdev_UI = cmds.menuItem( label= "LINDSEY" )
bruce_out_lookdev_UI = cmds.menuItem( label= "BRUCE OUT" )
willis_lookdev_UI = cmds.menuItem( label= "WILLIS WHITE" )
willis_red_lookdev_UI = cmds.menuItem( label= "WILLIS RED" )
tentacle_UI = cmds.menuItem( label= "TENTACLE" )
zodiac_UI = cmds.menuItem( label= "ZODIAC (020 only)" )

all_UI = cmds.checkBox( label = "All Characters", cc = change_vis_checkbox)



###### EXPORT BUTTONS
cmds.setParent (diUi["lays"]["exportButtons"])


start_frame_UI = cmds.textField(tx="950")
end_frame_UI = cmds.textField(tx="1001")
current_frame_UI = cmds.checkBox( label = "Export Current Frame", cc = change_vis_frame_range)
cmds.text( label= "  ")

# lindsey_box = cmds.checkBoxGrp( numberOfCheckBoxes=3, en=True, label='Lindsey', labelArray3=['Proxy', 'Groom', 'Cloth'], vr=True )
# bruce_box = cmds.checkBoxGrp( numberOfCheckBoxes=4, en=True, label='Bruce', labelArray4=['Light', 'Groom', 'Mask', 'Balls'], vr=True )
cmds.separator()
cmds.separator()

cmds.text(label = "Export Attributes")

cmds.text(label = "  ")
check_L_geo = cmds.checkBox( label='Lindsey Geo', v=True)
check_B_geo = cmds.checkBox( label='Bruce Geo', v=True)
check_L_groom = cmds.checkBox( label='Lindsey Groom', v=True)
check_B_groom = cmds.checkBox( label='Bruce Groom', v=True)
check_L_cloth = cmds.checkBox( label='Lindsey Cloth', v=True)
check_B_mask = cmds.checkBox( label='Bruce Mask', v=True)
cmds.text(label = "  ")
check_B_light = cmds.checkBox( label='Bruce Light')
cmds.text(label = "  ")
check_B_emitter = cmds.checkBox( label='Bruce Emitter')

tent_space_lbl = cmds.text(label = "Namespace if TENTACLE")
tent_space_text = cmds.textField(tx="TENT01")
any_space_lbl = cmds.text(label = "Namespace if CUSTOM", en=False)
any_space_text = cmds.textField(tx="CUSTOM (WIP)", en=False)



###### TEXT
# cmds.setParent (diUi["lays"]["text"])
cmds.button ( label = "Export CHARACTER(S)", backgroundColor=[0.0, 0.4, 0.4], c= export_char )

cmds.button ( label = "Export CUSTOM (Soon)", backgroundColor=[0.0, 0.4, 0.4], c= exportAnything, en=False )

# cmds.setParent (diUi["lays"]["cam"])

cmds.text(label="")
cmds.text(label="")
cmds.text( label= "Select cam if >> ")
cmds.button ( label = "Export CAMERA", backgroundColor=[0.0, 0.4, 0.4], c= exportBakeCamera )

#############################################################

cmds.setParent (diUi["lays"]["import"])
# BUTTONS
cmds.button ( label = "Import and Merge ABC", backgroundColor=[0.0, 0.4, 0.4], c= import_abc)
cmds.button ( label = "Import Camera", backgroundColor=[0.0, 0.4, 0.4], c= import_cam)

cmds.showWindow (diUi["window"]["main"])