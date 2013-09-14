using System;

namespace Domain
{
	public class Person
	{
		public int Age { get; set; }
		public string Name { get; set; }

		public Person()
		{
		}

		public override string ToString()
		{
			return string.Format("My name is {0}. I am {1}", Name, Age);
		}
	}
}

