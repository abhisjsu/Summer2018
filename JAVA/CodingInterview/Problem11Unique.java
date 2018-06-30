/*

Problem : To check if a given String has all unique charcaters or not

Standard and Extended ASCII Characters
	Total : 256
	Standard : 128 (all standard keyboard input keys are included here)
	Extended : 128


*/

public class Problem11Unique
{
	public static boolean checkUniqueBruteForce(String input)
	{
		int inputlength  = input.length();

		for(int i=0;i<inputlength;i++)
		{
			char current = input.charAt(i);
			for(int j=i+1;j<inputlength;j++)
			{
				if(input.charAt(j)==current)
					return false;
			}

		}

		return true;
	}

	public static boolean checkUniqueTimeOptimized(String input)
	{
		//There are total of 128 Standard ASCII Characters
		boolean check[] = new boolean[128];

		int inputlength  = input.length();

		for(int i=0;i<inputlength;i++)
		{
			int current = (int)input.charAt(i);
			if(check[current] == true)
				return false;
			check[current] = true;
		}
		return true;
	}


	public static void main(String argv[])
	{
		String inputVal1 = "helo";
		String inputVal2 = "hello";
		System.out.println("String : "+inputVal1+" unique : "+Problem11Unique.checkUniqueBruteForce(inputVal1));
		System.out.println("String : "+inputVal2+" unique : "+Problem11Unique.checkUniqueBruteForce(inputVal2));
		System.out.println("String : "+inputVal1+" unique : "+Problem11Unique.checkUniqueTimeOptimized(inputVal1));
		System.out.println("String : "+inputVal2+" unique : "+Problem11Unique.checkUniqueTimeOptimized(inputVal2));
	}
}