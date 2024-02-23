object Form1: TForm1
  Left = 0
  Top = 0
  AlphaBlend = True
  Caption = 'Evgeniy_Pelikh_IST-21-1'
  ClientHeight = 267
  ClientWidth = 522
  Color = clBackground
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  TextHeight = 13
  object Button1: TButton
    Left = 24
    Top = 184
    Width = 89
    Height = 40
    Caption = 'Close'
    TabOrder = 0
    OnClick = Button1Click
  end
  object BHeight: TButton
    Left = 168
    Top = 40
    Width = 83
    Height = 32
    Caption = '+ '#1042#1080#1089#1086#1090#1072
    Default = True
    TabOrder = 1
    OnClick = BHeightClick
  end
  object BWidth: TButton
    Left = 272
    Top = 40
    Width = 75
    Height = 32
    Cancel = True
    Caption = '+ '#1064#1080#1088#1080#1085#1072
    TabOrder = 2
    OnClick = BWidthClick
  end
  object BSize: TButton
    Left = 24
    Top = 130
    Width = 89
    Height = 33
    Caption = 'Default'
    TabOrder = 3
    OnClick = BSizeClick
  end
  object BXPlus: TButton
    Left = 272
    Top = 78
    Width = 75
    Height = 45
    Caption = #1055#1088#1072#1074#1086#1088#1091#1095' (+X)'
    TabOrder = 4
    OnClick = BXPlusClick
  end
  object BXMinus: TButton
    Left = 168
    Top = 78
    Width = 83
    Height = 45
    Caption = #1051#1110#1074#1086#1088#1091#1095' (-X)'
    TabOrder = 5
    OnClick = BXMinusClick
  end
  object BYPlus: TButton
    Left = 272
    Top = 129
    Width = 75
    Height = 36
    Caption = #1042#1085#1080#1079' (+Y)'
    TabOrder = 6
    OnClick = BYPlusClick
  end
  object BYMinus: TButton
    Left = 168
    Top = 129
    Width = 83
    Height = 36
    Caption = #1042#1075#1086#1088#1091' (-Y)'
    TabOrder = 7
    OnClick = BYMinusClick
  end
  object OpacityPlus: TButton
    Left = 272
    Top = 171
    Width = 75
    Height = 34
    Caption = '+ '#1055#1088#1086#1079#1086#1088#1110#1089#1090#1100
    TabOrder = 8
    OnClick = OpacityPlusClick
  end
  object OpacityMinus: TButton
    Left = 168
    Top = 171
    Width = 83
    Height = 34
    Caption = '- '#1055#1088#1086#1079#1086#1088#1110#1089#1090#1100
    TabOrder = 9
    OnClick = OpacityMinusClick
  end
end
