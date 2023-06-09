*** Settings ***

Library  main.py
Library  OperatingSystem
Library  Collections

*** Test Cases ***
Verify lifespan of the apps

*** Keywords ***
Verify lifespan of the apps

    ${output}=    Get File      output.yml
    ${info}=    Evaluate   yaml.load('''${output}''')
    ${nr_apps}=     Get Length  ${info}
    ${target}=  Set Variable  30
    ${lst}=   Create List
    ${percent}=  Set Variable  75
    ${apps_name}=  Create List
    FOR   ${apps}    IN      @{info.items()}
         ${lifespan}=   Set Variable    ${apps[1]['lifespan']}
         ${seconds}=    Evaluate    float('${lifespan}'.replace('s', ''))
         IF    ${seconds} < ${target}
            Append to List  ${lst}  ${seconds}
         ELSE
            IF    ${seconds} >= ${target}
                Append to List  ${apps_name}  ${apps[1]['app_path']}
            END
         END
    END
    ${length_lst}=  Get Length  ${lst}
    ${percentage}=  Evaluate  ${length_lst} / ${nr_apps} * 100.0
    IF   ${percentage}>=${percent}
        Pass Execution  Test Passed
    ELSE
        Log    Warning: The '${apps_name}' have the lifespan more than 30 seconds
        Fail    Less than 75% of the applications have the lifespan less than 30 seconds
    END
