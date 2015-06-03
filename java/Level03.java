/*
 * Level 3 of the python challenge
 */

import java.io.*; 
import java.io.Reader.*;
import java.util.regex.*;

public class Level03 {
	public static void main(String[] args) {
		try {
			BufferedReader br = new BufferedReader(new FileReader("Level03.txt"));
			String line, file = "";
			while ((line = br.readLine()) != null) {
				file += line;
			}

			// exactly 3 upper + 1 lower (group 1) + 3 upper caps
			Pattern p = Pattern.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]");
			Matcher m = p.matcher(file);

			// build the string from the matched group
			String s = "";
			while (m.find()) {
				s += m.group(1); // group 1 is the captured group
			}
			
			System.out.println("http://www.pythonchallenge.com/pc/def/" + s + ".html");
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}

}
