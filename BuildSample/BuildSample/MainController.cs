using System;

using MonoTouch.UIKit;
using MonoTouch.Foundation;

using Domain;

namespace BuildSample
{
	public class MainController : UIViewController
	{
		private UILabel _label;

		public MainController()
		{
		}

		public override void ViewDidLoad()
		{
			base.ViewDidLoad();
			View.BackgroundColor = UIColor.White;

			Person author = new Person
			{
				Age = 24,
				Name = "Rustam"
			};


			_label = new UILabel();
			_label.Text = author.ToString();
			_label.SizeToFit();


			View.AddSubview(_label);
			_label.Center = View.Center;
		}
	}
}
