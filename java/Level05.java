/*
 * Level 5 of Python Challenge
 */

import org.python.core.*;
import org.python.util.PythonInterpreter;
import java.io.*;
//import java.io.Writer.*;

public class Level05 {
	public static void main(String[] args) throws PyException, IOException {

		PythonInterpreter interp = new PythonInterpreter();
		
		/*
		 * The file to be used is a python pickle file.
		 * I'm using Jython here to import the pickle file.
		 */
		interp.exec("import pickle");
		interp.exec("pickle_file = open('banner.p', 'rb')"); // the banner.p can be found in the page source
		interp.exec("p = pickle.load(pickle_file)");
		interp.exec("pickle_file.close()");
		
		//I used this to see the actual structure of the pickle file
		//interp.exec("import pprint");
		//interp.exec("pp = pprint.PrettyPrinter(indent=4)");
		//interp.exec("pp.pprint(p)");

		// the output is larger than the console window (80 characters) :-(
		// print to a file
		PrintStream out = new PrintStream("Level05.txt");
		
		PyObject p = interp.get("p"); // convert the object "p" loaded from the pickle file to a java object
		PyList list = (PyList) p; // the object p is a python list structure
		// TODO: Maybe using iterators would be cleaner? I don't know... i like for loops.
		for (int i = 0; i < list.size(); i++) {
			PyList sublist = (PyList) list.get(i); // each element of the list is a sublist
			for (int j = 0; j < sublist.size(); j++) {
				PyTuple tuple = (PyTuple) sublist.get(j); // each element of the sublist is a tuple with two parts
				String string = (String) tuple.get(0); // the first part is a character to be printed
				int repeat = (int) tuple.get(1); // the second element is the number of times to print the character
				for (int k = 0; k < repeat; k++) {
					out.print(string);
				}
			}
			out.println();
		}
		out.close();
		
		// the final result is "channel"
	}
}
