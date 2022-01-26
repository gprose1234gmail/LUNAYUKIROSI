from Yukki import (ASS_CLI_1, ASSID1,  ASSNAME1, ASSUSERNAME1)
                   


async def get_assistant_details(assistant: int):
    if int(assistant) == 1:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = ASS_CLI_1
    
    return x, y, z, a
