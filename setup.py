import cx_Freeze

executables = [cx_Freeze.Executable("bomni.py")]

cx_Freeze.setup(
    name="Nuggy Snacks",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["fonts/Summer Beauty.otf", "images/banana1.bmp",
                                            "images/flipped.bmp", "images/jabolko1.bmp",
                                            "images/jagoda1.bmp", "images/lubenche1.bmp", 
                                            "images/nuggysit.bmp", "images/nuggystand_red.bmp",
                                            "sound effects/mixkit-game-ball-tap-2073.wav",
                                            "sound effects/mixkit-quick-jump-arcade-game-239.wav",
                                            "button.py", "nuggy.py", "ovoshje.py", "settings.py", "images/pink_background.webp"],}},
    executables = executables
    )