//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include <Vcl.Forms.hpp>


#include "Unit1.h"
#include "Unit2.h"
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
  Form2-> Show ();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
  Application-> Terminate ();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormShow(TObject *Sender)
{
  Application->MessageBox(L"Message text in the window",L"Test Message Window",MB_OK);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormActivate(TObject *Sender)
{
 ListBox1-> Items-> Add ( "FormActivate");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormDeactivate(TObject *Sender)
{
ListBox1-> Items-> Add ( "FormDeactivate");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormCloseQuery(TObject *Sender, bool &CanClose)
{
  if (Application-> MessageBox ( L"Do you really want to exit?",
  L"CloseQueryWindow", MB_OKCANCEL) == mrOk)
 CanClose = true;
 else
 CanClose = false;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormClose(TObject *Sender, TCloseAction &Action)
{
 Application-> MessageBox ( L"The form was closed",  L"Form closing...", MB_OK);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormPaint(TObject *Sender)
{
 ListBox1-> Items-> Add ( "FormPaint");
}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormResize(TObject *Sender)
{
  ListBox1-> Items-> Add ( "FormResize");
}
//---------------------------------------------------------------------------
