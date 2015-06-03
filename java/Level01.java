/**
 * Level 1 of the python challenge
 */
 
public class Level01 {
	public static void main(String[] args) {
		// the original encrypted string
		String s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " + 
		           "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " + 
				   "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
		String s2 = translateString(s);		
		System.out.println(s2);
		
		// the message suggest to apply this to the url, which is map		
		System.out.println("http://www.pythonchallenge.com/pc/def/" + translateString("map") + ".html");
	}
	
	private static String translateString(String s) {
		// the clue is: k->m, o->q, e->g
		// to decrypt the sequence you need to add 2 to every character in the range a-z
		char[] ca = s.toCharArray();
		for (int i = 0; i < s.length(); i++) {
			if (ca[i] >= 'a' && ca[i] <= 'z')
			  ca[i] += 2;
			if (ca[i] > 'z')
			  ca[i] -= 26;
		}		
		return new String(ca);
	}

}
