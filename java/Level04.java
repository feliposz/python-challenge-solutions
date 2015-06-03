/*
 * Level 4 of Python Challenge
 */

import java.io.*;
import java.io.Reader.*;
import java.net.*;
 
public class Level04 {
	public static void main(String[] args) {
		String next = "12345";
		String url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";
		String expected = "the next nothing is ";
		try {
			boolean found = false; // solution not found yet			
			while (!found) {
				// connect to the linkedlist url with the given parameter
				BufferedReader reader = new BufferedReader(new InputStreamReader(new URL(url + next).openStream()));
				String s;
				// check every line of the response
				while ((s = reader.readLine()) != null) {
					int i;
					if ((i = s.indexOf(expected)) != -1) { // check if there is a "the next nothing is" in the response body
						next = s.substring(i + expected.length());
						System.out.println(next);
						break;
					} else if (s.compareTo("Yes. Divide by two and keep going.") == 0) { // a special case in the linked list =)
						next = Integer.toString(Integer.parseInt(next) / 2);
						System.out.println(next);
						break;
					} else { // must be the solution... hmmm
						System.out.println("http://www.pythonchallenge.com/pc/def/" + s);
						found = true;
						break;
					}
				}				
			}			
		} catch (MalformedURLException mue) {
			System.out.println(mue.getMessage());
		} catch (IOException ie) {
			System.out.println(ie.getMessage());
		}
	}
	
}