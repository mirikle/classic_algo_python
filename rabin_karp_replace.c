string RemovePattern(string source, string pattern)
{
		StringBuilder b = new StringBuilder();

		int patternLength = pattern.Length;
		int patternHash = Hash(pattern, 0, patternLength-1);   

		int c = 0;
		while ((c + patternLength) < source.Length)
		{
				int sourceHash = Hash(source, c, patternLength - 1);
				if ((sourceHash == patternHash) && (pattern == source.SubStr(c, c + patternLength - 1))
				{
					c += patternLength;
				}
				else
				{
					builder.Append(string.CharAt(c));
					c++;
				}
		}
		return b.ToString();
}
