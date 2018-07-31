# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2

install(PROGRAMS "taste2rock_generator.py" DESTINATION "bin")
install(DIRECTORY "taste2rock"
        DESTINATION "lib/python"
        FILES_MATCHING 
        PATTERN "*.py" 
        PATTERN "*.mako"
        PATTERN "__pycache__" EXCLUDE)
