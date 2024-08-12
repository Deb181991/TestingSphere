        behave -f json -o Reports/my_json_out.json Features/Login.feature

        python custom_report_generator/report_generator.py --input_json_file Reports/my_json_out.json --output_html_file report1.html

        behave -f json -o Reports/my_json_out.json Features/Login.feature --no-capture --tags=LoginPage

        behave -f json -o Reports/my_json_out.json Features/Login.feature --no-capture --tags=LoginPage,CreateShipment
        python Features/runner.py Features/1Login.feature Features/2CELogin.feature

        For report--> behave -f allure_behave.formatter:AllureFormatter -o Reports Features/[Feature file name].feature
        For Report Generation-->allure serve Reports/



