package anemia;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RunPythonScripts {

    public static void main(String[] args) {
        try {
            // Command to run the python script with arguments
            String[] command = {
                   "python",
                    "C:\\FinalProject\\semangatProject\\anemia\\Anemia_cmd.py",
                    "male", // Gender
                    "13", //Hemoglobil
                    "48.3", // MCH
                    "30", // MCHC
                    "73" // MCV

            };

            // cd "C:\FinalProject\semangatProject\anemia"
            // javac RunPythonScripts.java
            // java "C:\FinalProject\semangatProject\anemia\RunPythonScripts.java"
            
            // Start the process
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.redirectErrorStream(true); // Combine standard output and error streams
            Process process = processBuilder.start();

            // Capture the output of the script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for the process to complete and get the exit status
            int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

    
