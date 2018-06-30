/*

Problem : To check if two given Strings are permutation of eachother

*/
import java.util.*;

public class Problem12CheckPermutation
{

	/*
	If the two Strings are permute their character XOR should cancel out
	*/
	public static boolean checkPermutationXOR(String input1,String input2)
	{	

		int input1Length = input1.length();
		int input2Length = input2.length();

		int result = 0;

		if(input1Length!=input2Length)
			return false;

		for(int i=0;i<input1Length;i++)
		{
			result ^=input1.charAt(i);
		}

		for(int i=0;i<input2Length;i++)
		{
			result ^=input2.charAt(i);
		}

		if(result ==0)
			return true;
		else
			return false;
	}

	/*
	If the two Strings are permute their Sort should resuts in same String 
	*/
	public static boolean checkPermutationBySort(String input1,String input2)
	{
		char input1Arr[] = input1.toCharArray();
		char input2Arr[] = input2.toCharArray();

		if(input1Arr.length != input2Arr.length)
			return false;

		Arrays.sort(input1Arr);
		Arrays.sort(input2Arr);

		input1= new String(input1Arr);
		input2= new String(input2Arr);

		if(input1.equals(input2))
			return true;
		else
			return false;

	}

	public static void main(String argv[])
	{
		System.out.println(Problem12CheckPermutation.checkPermutationXOR("helo","oelh"));
		System.out.println(Problem12CheckPermutation.checkPermutationXOR("helo","oelp"));
		System.out.println(Problem12CheckPermutation.checkPermutationBySort("helo","oelh"));
		System.out.println(Problem12CheckPermutation.checkPermutationBySort("helo","oelp"));
	}
}