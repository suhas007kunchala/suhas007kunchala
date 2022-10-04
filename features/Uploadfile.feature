Feature: upload file to Imgbb
  Scenario Outline: TC_105 Upload files
    Given user is on "<site>"
    Then user clicks on browse from computer
    Then user navigates to "<file>" and opens file
    Then user clicks on uplode button
    Then validate upload complete

    Examples:
      | site               | file                                                                |
      | https://imgbb.com/ | D:\ImpressicoProjects\BehavePlaywrightDemo\Resources\uploadfile.exe |
