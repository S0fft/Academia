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
void __fastcall TForm1::Button1Click(TObject *Sender)
{
 Close();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BHeightClick(TObject *Sender)
{
 Height = Height + 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BWidthClick(TObject *Sender)
{
Width = Width + 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BSizeClick(TObject *Sender)
{
Height = 500;
Width = 700;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BXMinusClick(TObject *Sender)
{
 Left = Left - 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BXPlusClick(TObject *Sender)
{
 Left = Left + 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BYMinusClick(TObject *Sender)
{
 Top = Top - 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BYPlusClick(TObject *Sender)
{
 Top = Top + 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::OpacityPlusClick(TObject *Sender)
{
  if (AlphaBlendValue <= 245)
AlphaBlendValue = AlphaBlendValue + 10;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::OpacityMinusClick(TObject *Sender)
{
if (AlphaBlendValue>= 10)
AlphaBlendValue = AlphaBlendValue - 10;
}
//---------------------------------------------------------------------------
