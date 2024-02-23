//---------------------------------------------------------------------------

#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TForm1 : public TForm
{
__published:	// IDE-managed Components
	TButton *Button1;
	TButton *BHeight;
	TButton *BWidth;
	TButton *BSize;
	TButton *BXPlus;
	TButton *BXMinus;
	TButton *BYPlus;
	TButton *BYMinus;
	TButton *OpacityPlus;
	TButton *OpacityMinus;
	void __fastcall Button1Click(TObject *Sender);
	void __fastcall BHeightClick(TObject *Sender);
	void __fastcall BWidthClick(TObject *Sender);
	void __fastcall BSizeClick(TObject *Sender);
	void __fastcall BXMinusClick(TObject *Sender);
	void __fastcall BXPlusClick(TObject *Sender);
	void __fastcall BYMinusClick(TObject *Sender);
	void __fastcall BYPlusClick(TObject *Sender);
	void __fastcall OpacityPlusClick(TObject *Sender);
	void __fastcall OpacityMinusClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TForm1(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
