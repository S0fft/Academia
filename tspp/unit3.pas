unit Unit3;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, ComCtrls,
  StdCtrls;

type

  { TForm3 }

  TForm3 = class(TForm)
    coImTriangle: TImage;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    tbX: TTrackBar;
    tbY: TTrackBar;
    tbSize: TTrackBar;
    procedure coImTriangleClick(Sender: TObject);
    procedure tbXChange(Sender: TObject);
    procedure tbYChange(Sender: TObject);
  private

  public

  end;

var
  Form3: TForm3;

implementation

function TForm1.CalculateSides(x, y, size: Integer; out side1, side2, side3: Double): Boolean;
var
  a, b, c: Double;
begin
  // Расчет длин сторон треугольника
  a := Hypot(size div 2, size);
  b := size;
  c := Hypot(size div 2, size);

  // Проверка существования треугольника по неравенству треугольника
  Result := (a + b > c) and (b + c > a) and (c + a > b);

  // Присвоение значений переменным, если треугольник существует
  if Result then
  begin
    side1 := a;
    side2 := b;
    side3 := c;
  end;
end;

  procedure TForm1.UpdateSideLengths;
  var
    side1, side2, side3: Double;
  begin
    if CalculateSides(tbX.Position, tbY.Position, tbSize.Position, side1, side2, side3) then
    begin
      // Вывод длин сторон в Edit'ы
      EditSide1.Text := Format('%.2f', [side1]);
      EditSide2.Text := Format('%.2f', [side2]);
      EditSide3.Text := Format('%.2f', [side3]);
    end
    else
    begin
      // Если треугольник не существует, очищаем Edit'ы
      EditSide1.Text := '';
      EditSide2.Text := '';
      EditSide3.Text := '';
    end;
  end;


{$R *.lfm}

{ TForm3 }

procedure TForm1.coImTrianglePaint(Sender: TObject);
var
  x, y, size: Integer;
begin
  x := tbX.Position;
  y := tbY.Position;
  size := tbSize.Position;

  DrawTriangle(x, y, size);
end;

procedure TForm1.coImTrianglePaint(Sender: TObject);
var
  x, y, size: Integer;
begin
  x := tbX.Position;
  y := tbY.Position;
  size := tbSize.Position;

  DrawTriangle(x, y, size);
end;

procedure TForm3.DrawTriangle(x, y, size: Integer);
begin
  with coImTriangle.Canvas do
  begin
    // Очистка рисунка
    Brush.Color := clWhite;
    FillRect(0, 0, coImTriangle.Width, coImTriangle.Height);

    // Рисование треугольника
    if CalculateSides(x, y, size, Side1, Side2, Side3) then
    begin
      Pen.Color := clBlack;  // Черная сторона
      Brush.Color := clBlack;
      Polygon([Point(x, y), Point(x + size, y), Point(x + size div 2, y + size)]);

      Pen.Color := clRed;    // Красная сторона
      Brush.Color := clRed;
      Polygon([Point(x + size, y), Point(x + size div 2, y + size), Point(x + size * 2, y + size)]);

      Pen.Color := clBlue;   // Синяя сторона
      Brush.Color := clBlue;
      Polygon([Point(x + size div 2, y + size), Point(x + size * 2, y + size), Point(x + size, y + size * 2)]);
    end;
  end;
end;


procedure TForm3.coImTriangleClick(Sender: TObject);
begin

end;

procedure TForm3.tbXChange(Sender: TObject);
begin
  coImTriangle.Invalidate;  // Вызывает событие OnPaint для перерисовки
end;


procedure TForm3.tbYChange(Sender: TObject);
begin
  coImTriangle.Invalidate;  // Вызывает событие OnPaint для перерисовки
end;

public
  procedure DrawTriangle(x, y, size: Integer);
  function CalculateSides(x, y, size: Integer; out side1, side2, side3: Double): Boolean;

end.

