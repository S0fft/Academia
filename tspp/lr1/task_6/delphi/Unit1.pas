unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    LX: TLabel;
    LY: TLabel;
    ListBox1: TListBox;
    procedure FormMouseEnter(Sender: TObject);
    procedure FormMouseLeave(Sender: TObject);
    procedure FormMouseMove(Sender: TObject; Shift: TShiftState; X, Y: Integer);
    procedure FormMouseWheel(Sender: TObject; Shift: TShiftState;
      WheelDelta: Integer; MousePos: TPoint; var Handled: Boolean);
    procedure FormMouseWheelDown(Sender: TObject; Shift: TShiftState;
      MousePos: TPoint; var Handled: Boolean);
    procedure FormMouseWheelUp(Sender: TObject; Shift: TShiftState;
      MousePos: TPoint; var Handled: Boolean);
    procedure FormClick(Sender: TObject);
    procedure FormDblClick(Sender: TObject);
    procedure FormMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure FormMouseUp(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.FormClick(Sender: TObject);
begin
  ListBox1.Items.Add ( 'OnClick');
end;

procedure TForm1.FormDblClick(Sender: TObject);
begin
ListBox1.Items.Add ( 'OnDblClick');
end;

procedure TForm1.FormMouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
  var S: String;
begin
  if (Button = mbLeft) then
 S:= 'Left';
 if (Button = mbRight) then
 S:= 'Right';
 if (Button = mbMiddle) then
 S:= 'Middle';
  ListBox1.Items.Add ( 'OnMouseDown' + S +
 ', X =' + IntToStr (X) +
 ', Y =' + IntToStr (Y));
  if (ssShift in Shift) then
 ListBox1.Items.Add ( '++ Shift');
 if (ssCtrl in Shift) then
 ListBox1.Items.Add ( '++ Ctrl');
 if (ssAlt in Shift) then
 ListBox1.Items.Add ( '++ Alt');
end;

procedure TForm1.FormMouseEnter(Sender: TObject);
begin
  ListBox1.Items.Add ( 'FormMouseEnter');
end;

procedure TForm1.FormMouseLeave(Sender: TObject);
begin
ListBox1.Items.Add ( 'FormMouseLeave');
end;

procedure TForm1.FormMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
begin
  LX.Caption:= IntToStr (X);
 LY.Caption:= IntToStr (Y);
end;

procedure TForm1.FormMouseUp(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
  var S: String;
begin
   if (Button = mbLeft) then
 S:= 'Left';
 if (Button = mbRight) then
 S:= 'Right';
 if (Button = mbMiddle) then
 S:= 'Middle';
 ListBox1.Items.Add ( 'OnMouseUp' + S +
 ', X =' + IntToStr (X) +
 ', Y =' + IntToStr (Y));
  if (ssShift in Shift) then
 ListBox1.Items.Add ( '++ Shift');
 if (ssCtrl in Shift) then
 ListBox1.Items.Add ( '++ Ctrl');
 if (ssAlt in Shift) then
 ListBox1.Items.Add ( '++ Alt');
end;

procedure TForm1.FormMouseWheel(Sender: TObject; Shift: TShiftState;
  WheelDelta: Integer; MousePos: TPoint; var Handled: Boolean);
begin
  ListBox1.Items.Add ( 'FormMouseWheel, WheelDelta =' + IntToStr (WheelDelta));
end;

procedure TForm1.FormMouseWheelDown(Sender: TObject; Shift: TShiftState;
  MousePos: TPoint; var Handled: Boolean);
begin
   ListBox1.Items.Add ( 'FormMouseWheelDown. X =' +
 IntToStr (MousePos.X) + ', Y =' + IntToStr (MousePos.Y));
end;

procedure TForm1.FormMouseWheelUp(Sender: TObject; Shift: TShiftState;
  MousePos: TPoint; var Handled: Boolean);
begin
  ListBox1.Items.Add ( 'FormMouseWheelUp. X =' +
 IntToStr (MousePos.X) + ', Y =' + IntToStr (MousePos.Y));
end;

end.
