/**
 * Level 2 of the python challenge
 */

import java.io.*; 
import java.io.Reader.*;
 
public class Level02 {
	public static void main(String[] args) {
		try {
			System.out.println("Opening file.");
			FileReader fr = new FileReader("Level02.txt");

			System.out.println("Reading file to generate histogram.");
			int c;
			int[] histogram = new int[256];
			while ((c = fr.read()) != -1) {
				histogram[c]++;
			}

			System.out.println("Histogram");
			for (int i = 0; i < 256; i++) {
				if (histogram[i] > 0) {
					System.out.println((char)i + ": " + histogram[i]);
				}
			}

			System.out.println("Resetting file.");
			fr.close();
			fr = new FileReader("Level02.txt");

			String s = "";
			System.out.println("Get rare characters");
			while ((c = fr.read()) != -1) {
				if (histogram[c] == 1) {
					//System.out.print((char) c);
					s += (char)c;
				}
			}			
			
			System.out.println("http://www.pythonchallenge.com/pc/def/" + s + ".html");
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}

}
