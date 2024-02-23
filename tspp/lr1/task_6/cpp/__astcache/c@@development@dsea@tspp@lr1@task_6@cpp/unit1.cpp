//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseEnter(TObject *Sender)
{
ListBox1-> Items-> Add ( "FormMouseEnter");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseLeave(TObject *Sender)
{
ListBox1-> Items-> Add ( "FormMouseLeave");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseMove(TObject *Sender, TShiftState Shift, int X, int Y)

{
  LX-> Caption = IntToStr (X);
 LY-> Caption = IntToStr (Y);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseWheel(TObject *Sender, TShiftState Shift, int WheelDelta,
          TPoint &MousePos, bool &Handled)
{
  ListBox1-> Items-> Add ( "FormMouseWheel, WheelDelta =" + IntToStr (WheelDelta));
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseWheelUp(TObject *Sender, TShiftState Shift, TPoint &MousePos,
          bool &Handled)
{
 ListBox1-> Items-> Add ( "FormMouseWheelUp. X =" +
IntToStr (__int64 (MousePos.x)) + ", Y =" +
IntToStr (__int64 (MousePos.y)));
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseWheelDown(TObject *Sender, TShiftState Shift, TPoint &MousePos,
          bool &Handled)
{
 ListBox1-> Items-> Add ( "FormMouseWheelDown. X =" +
IntToStr (__int64 (MousePos.x)) + ", Y =" +
 IntToStr (__int64 (MousePos.y)));
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormClick(TObject *Sender)
{
  ListBox1-> Items-> Add ( "OnClick");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormDblClick(TObject *Sender)
{
 ListBox1-> Items-> Add ( "OnDblClick");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseDown(TObject *Sender, TMouseButton Button, TShiftState Shift,
          int X, int Y)
{
  AnsiString S;
 if (Button == mbLeft)
 S = "Left";
 if (Button == mbRight)
 S = "Right";
 if (Button == mbMiddle)
 S = "Middle";
 ListBox1-> Items-> Add ( "OnMouseDown" + S +
 ", X =" + IntToStr (X) +
 ", Y =" + IntToStr (Y));
 if (Shift.Contains (ssShift))
 ListBox1-> Items-> Add ( "++ Shift");
 if (Shift.Contains (ssCtrl))
 ListBox1-> Items-> Add ( "++ Ctrl");
 if (Shift.Contains (ssAlt))
 ListBox1-> Items-> Add ( "++ Alt");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormMouseUp(TObject *Sender, TMouseButton Button, TShiftState Shift,
          int X, int Y)
{
 AnsiString S;
 if (Button == mbLeft)
 S = "Left";
 if (Button == mbRight)
 S = "Right";
 if (Button == mbMiddle)
 S = "Middle";
 ListBox1-> Items-> Add ( "OnMouseUp" + S +
 ", X =" + IntToStr (X) +
 ", Y =" + IntToStr (Y));
  if (Shift.Contains (ssShift))
 ListBox1-> Items-> Add ( "++ Shift");
 if (Shift.Contains (ssCtrl))
 ListBox1-> Items-> Add ( "++ Ctrl");
 if (Shift.Contains (ssAlt))
 ListBox1-> Items-> Add ( "++ Alt");
}
//---------------------------------------------------------------------------
