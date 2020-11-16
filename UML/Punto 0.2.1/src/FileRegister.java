import java.io.File;  // Import the File class
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

public class FileRegister implements Register{
	
	@Override
	public void getRegister(String message) {
		System.out.println(">> File Register!!");
		createFile();
		writeMessage(message);
		
	}
	
	public void createFile() { //Codigo tomado de https://www.w3schools.com/java/java_files_create.asp
		try {
		      File myObj = new File("src/fileOutput/fileRegister.txt");
		      if (myObj.createNewFile()) {
		        System.out.println("File created: " + myObj.getName());
		      } else {
		        System.out.println("File already exists.");
		      }
		    } catch (IOException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		
	}
	
	public void writeMessage (String message) { //Codigo tomado de https://www.w3schools.com/java/java_files_create.asp
		try {
		      FileWriter myWriter = new FileWriter("src/fileOutput/fileRegister.txt");
		      myWriter.write(message + "\n");
		      myWriter.close();
		      System.out.println("Successfully wrote to the file.");
		    } catch (IOException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		
	}

}
