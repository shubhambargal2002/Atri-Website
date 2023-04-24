from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.TextBox import TextBox
from atri_react.Image import Image
from atri_react.Button import Button
from atri_react.Div import Div


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.Button1 = state["Button1"] if "Button1" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.Button2 = state["Button2"] if "Button2" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.Div2 = state["Div2"] if "Div2" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.Image21 = state["Image21"] if "Image21" in state else None
		self.Image23 = state["Image23"] if "Image23" in state else None
		self.Image24 = state["Image24"] if "Image24" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.Image27 = state["Image27"] if "Image27" in state else None
		self.Image28 = state["Image28"] if "Image28" in state else None
		self.Image30 = state["Image30"] if "Image30" in state else None
		self.Image31 = state["Image31"] if "Image31" in state else None
		self.Image32 = state["Image32"] if "Image32" in state else None
		self.Image33 = state["Image33"] if "Image33" in state else None
		self.Image34 = state["Image34"] if "Image34" in state else None
		self.Image36 = state["Image36"] if "Image36" in state else None
		self.Image37 = state["Image37"] if "Image37" in state else None
		self.Image39 = state["Image39"] if "Image39" in state else None
		self.Image40 = state["Image40"] if "Image40" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.Image41 = state["Image41"] if "Image41" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Image42 = state["Image42"] if "Image42" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Image43 = state["Image43"] if "Image43" in state else None
		self.Image44 = state["Image44"] if "Image44" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.Image45 = state["Image45"] if "Image45" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.Image46 = state["Image46"] if "Image46" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.Image47 = state["Image47"] if "Image47" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.Image49 = state["Image49"] if "Image49" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.Image53 = state["Image53"] if "Image53" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.Image54 = state["Image54"] if "Image54" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.Image55 = state["Image55"] if "Image55" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.Image56 = state["Image56"] if "Image56" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.Image57 = state["Image57"] if "Image57" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Image58 = state["Image58"] if "Image58" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Image59 = state["Image59"] if "Image59" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Flex65 = state["Flex65"] if "Flex65" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.Image60 = state["Image60"] if "Image60" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Flex68 = state["Flex68"] if "Flex68" in state else None
		self.Image61 = state["Image61"] if "Image61" in state else None
		self.Flex69 = state["Flex69"] if "Flex69" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.Flex70 = state["Flex70"] if "Flex70" in state else None
		self.Flex71 = state["Flex71"] if "Flex71" in state else None
		self.Flex72 = state["Flex72"] if "Flex72" in state else None
		self.Flex73 = state["Flex73"] if "Flex73" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.TextBox47 = state["TextBox47"] if "TextBox47" in state else None
		self.Image62 = state["Image62"] if "Image62" in state else None
		self.Flex74 = state["Flex74"] if "Flex74" in state else None
		self.Flex75 = state["Flex75"] if "Flex75" in state else None
		self.Image63 = state["Image63"] if "Image63" in state else None
		self.Flex76 = state["Flex76"] if "Flex76" in state else None
		self.TextBox48 = state["TextBox48"] if "TextBox48" in state else None
		self.TextBox49 = state["TextBox49"] if "TextBox49" in state else None
		self.Flex77 = state["Flex77"] if "Flex77" in state else None
		self.Flex78 = state["Flex78"] if "Flex78" in state else None
		self.Flex79 = state["Flex79"] if "Flex79" in state else None
		self.Flex80 = state["Flex80"] if "Flex80" in state else None
		self.Image64 = state["Image64"] if "Image64" in state else None
		self.TextBox50 = state["TextBox50"] if "TextBox50" in state else None
		self.TextBox51 = state["TextBox51"] if "TextBox51" in state else None
		self.TextBox52 = state["TextBox52"] if "TextBox52" in state else None
		self.TextBox53 = state["TextBox53"] if "TextBox53" in state else None
		self.Image65 = state["Image65"] if "Image65" in state else None
		self.Image66 = state["Image66"] if "Image66" in state else None
		self.Flex81 = state["Flex81"] if "Flex81" in state else None
		self.Flex82 = state["Flex82"] if "Flex82" in state else None
		self.Image67 = state["Image67"] if "Image67" in state else None
		self.Flex83 = state["Flex83"] if "Flex83" in state else None
		self.TextBox54 = state["TextBox54"] if "TextBox54" in state else None
		self.TextBox55 = state["TextBox55"] if "TextBox55" in state else None
		self.Flex84 = state["Flex84"] if "Flex84" in state else None
		self.Flex85 = state["Flex85"] if "Flex85" in state else None
		self.Flex86 = state["Flex86"] if "Flex86" in state else None
		self.Flex87 = state["Flex87"] if "Flex87" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.TextBox58 = state["TextBox58"] if "TextBox58" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.Image68 = state["Image68"] if "Image68" in state else None
		self.Flex88 = state["Flex88"] if "Flex88" in state else None
		self.Flex89 = state["Flex89"] if "Flex89" in state else None
		self.Image69 = state["Image69"] if "Image69" in state else None
		self.Flex90 = state["Flex90"] if "Flex90" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.TextBox61 = state["TextBox61"] if "TextBox61" in state else None
		self.Flex91 = state["Flex91"] if "Flex91" in state else None
		self.Flex92 = state["Flex92"] if "Flex92" in state else None
		self.Flex93 = state["Flex93"] if "Flex93" in state else None
		self.Flex94 = state["Flex94"] if "Flex94" in state else None
		self.Image71 = state["Image71"] if "Image71" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		self._Flex1 = Flex(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def Button1(self):
		self._getter_access_tracker["Button1"] = {}
		return self._Button1
	@Button1.setter
	def Button1(self, new_state):
		self._setter_access_tracker["Button1"] = {}
		self._Button1 = Button(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def Button2(self):
		self._getter_access_tracker["Button2"] = {}
		return self._Button2
	@Button2.setter
	def Button2(self, new_state):
		self._setter_access_tracker["Button2"] = {}
		self._Button2 = Button(new_state)

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def Div2(self):
		self._getter_access_tracker["Div2"] = {}
		return self._Div2
	@Div2.setter
	def Div2(self, new_state):
		self._setter_access_tracker["Div2"] = {}
		self._Div2 = Div(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def Flex34(self):
		self._getter_access_tracker["Flex34"] = {}
		return self._Flex34
	@Flex34.setter
	def Flex34(self, new_state):
		self._setter_access_tracker["Flex34"] = {}
		self._Flex34 = Flex(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		self._Image21 = Image(new_state)

	@property
	def Image23(self):
		self._getter_access_tracker["Image23"] = {}
		return self._Image23
	@Image23.setter
	def Image23(self, new_state):
		self._setter_access_tracker["Image23"] = {}
		self._Image23 = Image(new_state)

	@property
	def Image24(self):
		self._getter_access_tracker["Image24"] = {}
		return self._Image24
	@Image24.setter
	def Image24(self, new_state):
		self._setter_access_tracker["Image24"] = {}
		self._Image24 = Image(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		self._Flex37 = Flex(new_state)

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		self._Flex38 = Flex(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		self._Flex39 = Flex(new_state)

	@property
	def Image27(self):
		self._getter_access_tracker["Image27"] = {}
		return self._Image27
	@Image27.setter
	def Image27(self, new_state):
		self._setter_access_tracker["Image27"] = {}
		self._Image27 = Image(new_state)

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		self._Image28 = Image(new_state)

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		self._Image30 = Image(new_state)

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		self._Image31 = Image(new_state)

	@property
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		self._Image32 = Image(new_state)

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		self._Image33 = Image(new_state)

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		self._Image34 = Image(new_state)

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		self._Image36 = Image(new_state)

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		self._Image37 = Image(new_state)

	@property
	def Image39(self):
		self._getter_access_tracker["Image39"] = {}
		return self._Image39
	@Image39.setter
	def Image39(self, new_state):
		self._setter_access_tracker["Image39"] = {}
		self._Image39 = Image(new_state)

	@property
	def Image40(self):
		self._getter_access_tracker["Image40"] = {}
		return self._Image40
	@Image40.setter
	def Image40(self, new_state):
		self._setter_access_tracker["Image40"] = {}
		self._Image40 = Image(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def Image41(self):
		self._getter_access_tracker["Image41"] = {}
		return self._Image41
	@Image41.setter
	def Image41(self, new_state):
		self._setter_access_tracker["Image41"] = {}
		self._Image41 = Image(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def Image42(self):
		self._getter_access_tracker["Image42"] = {}
		return self._Image42
	@Image42.setter
	def Image42(self, new_state):
		self._setter_access_tracker["Image42"] = {}
		self._Image42 = Image(new_state)

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		self._Flex41 = Flex(new_state)

	@property
	def Flex42(self):
		self._getter_access_tracker["Flex42"] = {}
		return self._Flex42
	@Flex42.setter
	def Flex42(self, new_state):
		self._setter_access_tracker["Flex42"] = {}
		self._Flex42 = Flex(new_state)

	@property
	def Image43(self):
		self._getter_access_tracker["Image43"] = {}
		return self._Image43
	@Image43.setter
	def Image43(self, new_state):
		self._setter_access_tracker["Image43"] = {}
		self._Image43 = Image(new_state)

	@property
	def Image44(self):
		self._getter_access_tracker["Image44"] = {}
		return self._Image44
	@Image44.setter
	def Image44(self, new_state):
		self._setter_access_tracker["Image44"] = {}
		self._Image44 = Image(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		self._Flex46 = Flex(new_state)

	@property
	def Image45(self):
		self._getter_access_tracker["Image45"] = {}
		return self._Image45
	@Image45.setter
	def Image45(self, new_state):
		self._setter_access_tracker["Image45"] = {}
		self._Image45 = Image(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def Image46(self):
		self._getter_access_tracker["Image46"] = {}
		return self._Image46
	@Image46.setter
	def Image46(self, new_state):
		self._setter_access_tracker["Image46"] = {}
		self._Image46 = Image(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def Image47(self):
		self._getter_access_tracker["Image47"] = {}
		return self._Image47
	@Image47.setter
	def Image47(self, new_state):
		self._setter_access_tracker["Image47"] = {}
		self._Image47 = Image(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def Image49(self):
		self._getter_access_tracker["Image49"] = {}
		return self._Image49
	@Image49.setter
	def Image49(self, new_state):
		self._setter_access_tracker["Image49"] = {}
		self._Image49 = Image(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def Image53(self):
		self._getter_access_tracker["Image53"] = {}
		return self._Image53
	@Image53.setter
	def Image53(self, new_state):
		self._setter_access_tracker["Image53"] = {}
		self._Image53 = Image(new_state)

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def Image54(self):
		self._getter_access_tracker["Image54"] = {}
		return self._Image54
	@Image54.setter
	def Image54(self, new_state):
		self._setter_access_tracker["Image54"] = {}
		self._Image54 = Image(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def Image55(self):
		self._getter_access_tracker["Image55"] = {}
		return self._Image55
	@Image55.setter
	def Image55(self, new_state):
		self._setter_access_tracker["Image55"] = {}
		self._Image55 = Image(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def Image56(self):
		self._getter_access_tracker["Image56"] = {}
		return self._Image56
	@Image56.setter
	def Image56(self, new_state):
		self._setter_access_tracker["Image56"] = {}
		self._Image56 = Image(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

	@property
	def Image57(self):
		self._getter_access_tracker["Image57"] = {}
		return self._Image57
	@Image57.setter
	def Image57(self, new_state):
		self._setter_access_tracker["Image57"] = {}
		self._Image57 = Image(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Image58(self):
		self._getter_access_tracker["Image58"] = {}
		return self._Image58
	@Image58.setter
	def Image58(self, new_state):
		self._setter_access_tracker["Image58"] = {}
		self._Image58 = Image(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def TextBox32(self):
		self._getter_access_tracker["TextBox32"] = {}
		return self._TextBox32
	@TextBox32.setter
	def TextBox32(self, new_state):
		self._setter_access_tracker["TextBox32"] = {}
		self._TextBox32 = TextBox(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Image59(self):
		self._getter_access_tracker["Image59"] = {}
		return self._Image59
	@Image59.setter
	def Image59(self, new_state):
		self._setter_access_tracker["Image59"] = {}
		self._Image59 = Image(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Flex65(self):
		self._getter_access_tracker["Flex65"] = {}
		return self._Flex65
	@Flex65.setter
	def Flex65(self, new_state):
		self._setter_access_tracker["Flex65"] = {}
		self._Flex65 = Flex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		self._TextBox38 = TextBox(new_state)

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		self._TextBox39 = TextBox(new_state)

	@property
	def TextBox40(self):
		self._getter_access_tracker["TextBox40"] = {}
		return self._TextBox40
	@TextBox40.setter
	def TextBox40(self, new_state):
		self._setter_access_tracker["TextBox40"] = {}
		self._TextBox40 = TextBox(new_state)

	@property
	def TextBox41(self):
		self._getter_access_tracker["TextBox41"] = {}
		return self._TextBox41
	@TextBox41.setter
	def TextBox41(self, new_state):
		self._setter_access_tracker["TextBox41"] = {}
		self._TextBox41 = TextBox(new_state)

	@property
	def Image60(self):
		self._getter_access_tracker["Image60"] = {}
		return self._Image60
	@Image60.setter
	def Image60(self, new_state):
		self._setter_access_tracker["Image60"] = {}
		self._Image60 = Image(new_state)

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		self._Flex68 = Flex(new_state)

	@property
	def Image61(self):
		self._getter_access_tracker["Image61"] = {}
		return self._Image61
	@Image61.setter
	def Image61(self, new_state):
		self._setter_access_tracker["Image61"] = {}
		self._Image61 = Image(new_state)

	@property
	def Flex69(self):
		self._getter_access_tracker["Flex69"] = {}
		return self._Flex69
	@Flex69.setter
	def Flex69(self, new_state):
		self._setter_access_tracker["Flex69"] = {}
		self._Flex69 = Flex(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		self._TextBox43 = TextBox(new_state)

	@property
	def Flex70(self):
		self._getter_access_tracker["Flex70"] = {}
		return self._Flex70
	@Flex70.setter
	def Flex70(self, new_state):
		self._setter_access_tracker["Flex70"] = {}
		self._Flex70 = Flex(new_state)

	@property
	def Flex71(self):
		self._getter_access_tracker["Flex71"] = {}
		return self._Flex71
	@Flex71.setter
	def Flex71(self, new_state):
		self._setter_access_tracker["Flex71"] = {}
		self._Flex71 = Flex(new_state)

	@property
	def Flex72(self):
		self._getter_access_tracker["Flex72"] = {}
		return self._Flex72
	@Flex72.setter
	def Flex72(self, new_state):
		self._setter_access_tracker["Flex72"] = {}
		self._Flex72 = Flex(new_state)

	@property
	def Flex73(self):
		self._getter_access_tracker["Flex73"] = {}
		return self._Flex73
	@Flex73.setter
	def Flex73(self, new_state):
		self._setter_access_tracker["Flex73"] = {}
		self._Flex73 = Flex(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def TextBox47(self):
		self._getter_access_tracker["TextBox47"] = {}
		return self._TextBox47
	@TextBox47.setter
	def TextBox47(self, new_state):
		self._setter_access_tracker["TextBox47"] = {}
		self._TextBox47 = TextBox(new_state)

	@property
	def Image62(self):
		self._getter_access_tracker["Image62"] = {}
		return self._Image62
	@Image62.setter
	def Image62(self, new_state):
		self._setter_access_tracker["Image62"] = {}
		self._Image62 = Image(new_state)

	@property
	def Flex74(self):
		self._getter_access_tracker["Flex74"] = {}
		return self._Flex74
	@Flex74.setter
	def Flex74(self, new_state):
		self._setter_access_tracker["Flex74"] = {}
		self._Flex74 = Flex(new_state)

	@property
	def Flex75(self):
		self._getter_access_tracker["Flex75"] = {}
		return self._Flex75
	@Flex75.setter
	def Flex75(self, new_state):
		self._setter_access_tracker["Flex75"] = {}
		self._Flex75 = Flex(new_state)

	@property
	def Image63(self):
		self._getter_access_tracker["Image63"] = {}
		return self._Image63
	@Image63.setter
	def Image63(self, new_state):
		self._setter_access_tracker["Image63"] = {}
		self._Image63 = Image(new_state)

	@property
	def Flex76(self):
		self._getter_access_tracker["Flex76"] = {}
		return self._Flex76
	@Flex76.setter
	def Flex76(self, new_state):
		self._setter_access_tracker["Flex76"] = {}
		self._Flex76 = Flex(new_state)

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		self._TextBox48 = TextBox(new_state)

	@property
	def TextBox49(self):
		self._getter_access_tracker["TextBox49"] = {}
		return self._TextBox49
	@TextBox49.setter
	def TextBox49(self, new_state):
		self._setter_access_tracker["TextBox49"] = {}
		self._TextBox49 = TextBox(new_state)

	@property
	def Flex77(self):
		self._getter_access_tracker["Flex77"] = {}
		return self._Flex77
	@Flex77.setter
	def Flex77(self, new_state):
		self._setter_access_tracker["Flex77"] = {}
		self._Flex77 = Flex(new_state)

	@property
	def Flex78(self):
		self._getter_access_tracker["Flex78"] = {}
		return self._Flex78
	@Flex78.setter
	def Flex78(self, new_state):
		self._setter_access_tracker["Flex78"] = {}
		self._Flex78 = Flex(new_state)

	@property
	def Flex79(self):
		self._getter_access_tracker["Flex79"] = {}
		return self._Flex79
	@Flex79.setter
	def Flex79(self, new_state):
		self._setter_access_tracker["Flex79"] = {}
		self._Flex79 = Flex(new_state)

	@property
	def Flex80(self):
		self._getter_access_tracker["Flex80"] = {}
		return self._Flex80
	@Flex80.setter
	def Flex80(self, new_state):
		self._setter_access_tracker["Flex80"] = {}
		self._Flex80 = Flex(new_state)

	@property
	def Image64(self):
		self._getter_access_tracker["Image64"] = {}
		return self._Image64
	@Image64.setter
	def Image64(self, new_state):
		self._setter_access_tracker["Image64"] = {}
		self._Image64 = Image(new_state)

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		self._TextBox50 = TextBox(new_state)

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		self._TextBox51 = TextBox(new_state)

	@property
	def TextBox52(self):
		self._getter_access_tracker["TextBox52"] = {}
		return self._TextBox52
	@TextBox52.setter
	def TextBox52(self, new_state):
		self._setter_access_tracker["TextBox52"] = {}
		self._TextBox52 = TextBox(new_state)

	@property
	def TextBox53(self):
		self._getter_access_tracker["TextBox53"] = {}
		return self._TextBox53
	@TextBox53.setter
	def TextBox53(self, new_state):
		self._setter_access_tracker["TextBox53"] = {}
		self._TextBox53 = TextBox(new_state)

	@property
	def Image65(self):
		self._getter_access_tracker["Image65"] = {}
		return self._Image65
	@Image65.setter
	def Image65(self, new_state):
		self._setter_access_tracker["Image65"] = {}
		self._Image65 = Image(new_state)

	@property
	def Image66(self):
		self._getter_access_tracker["Image66"] = {}
		return self._Image66
	@Image66.setter
	def Image66(self, new_state):
		self._setter_access_tracker["Image66"] = {}
		self._Image66 = Image(new_state)

	@property
	def Flex81(self):
		self._getter_access_tracker["Flex81"] = {}
		return self._Flex81
	@Flex81.setter
	def Flex81(self, new_state):
		self._setter_access_tracker["Flex81"] = {}
		self._Flex81 = Flex(new_state)

	@property
	def Flex82(self):
		self._getter_access_tracker["Flex82"] = {}
		return self._Flex82
	@Flex82.setter
	def Flex82(self, new_state):
		self._setter_access_tracker["Flex82"] = {}
		self._Flex82 = Flex(new_state)

	@property
	def Image67(self):
		self._getter_access_tracker["Image67"] = {}
		return self._Image67
	@Image67.setter
	def Image67(self, new_state):
		self._setter_access_tracker["Image67"] = {}
		self._Image67 = Image(new_state)

	@property
	def Flex83(self):
		self._getter_access_tracker["Flex83"] = {}
		return self._Flex83
	@Flex83.setter
	def Flex83(self, new_state):
		self._setter_access_tracker["Flex83"] = {}
		self._Flex83 = Flex(new_state)

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		self._TextBox54 = TextBox(new_state)

	@property
	def TextBox55(self):
		self._getter_access_tracker["TextBox55"] = {}
		return self._TextBox55
	@TextBox55.setter
	def TextBox55(self, new_state):
		self._setter_access_tracker["TextBox55"] = {}
		self._TextBox55 = TextBox(new_state)

	@property
	def Flex84(self):
		self._getter_access_tracker["Flex84"] = {}
		return self._Flex84
	@Flex84.setter
	def Flex84(self, new_state):
		self._setter_access_tracker["Flex84"] = {}
		self._Flex84 = Flex(new_state)

	@property
	def Flex85(self):
		self._getter_access_tracker["Flex85"] = {}
		return self._Flex85
	@Flex85.setter
	def Flex85(self, new_state):
		self._setter_access_tracker["Flex85"] = {}
		self._Flex85 = Flex(new_state)

	@property
	def Flex86(self):
		self._getter_access_tracker["Flex86"] = {}
		return self._Flex86
	@Flex86.setter
	def Flex86(self, new_state):
		self._setter_access_tracker["Flex86"] = {}
		self._Flex86 = Flex(new_state)

	@property
	def Flex87(self):
		self._getter_access_tracker["Flex87"] = {}
		return self._Flex87
	@Flex87.setter
	def Flex87(self, new_state):
		self._setter_access_tracker["Flex87"] = {}
		self._Flex87 = Flex(new_state)

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		self._TextBox56 = TextBox(new_state)

	@property
	def TextBox57(self):
		self._getter_access_tracker["TextBox57"] = {}
		return self._TextBox57
	@TextBox57.setter
	def TextBox57(self, new_state):
		self._setter_access_tracker["TextBox57"] = {}
		self._TextBox57 = TextBox(new_state)

	@property
	def TextBox58(self):
		self._getter_access_tracker["TextBox58"] = {}
		return self._TextBox58
	@TextBox58.setter
	def TextBox58(self, new_state):
		self._setter_access_tracker["TextBox58"] = {}
		self._TextBox58 = TextBox(new_state)

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		self._TextBox59 = TextBox(new_state)

	@property
	def Image68(self):
		self._getter_access_tracker["Image68"] = {}
		return self._Image68
	@Image68.setter
	def Image68(self, new_state):
		self._setter_access_tracker["Image68"] = {}
		self._Image68 = Image(new_state)

	@property
	def Flex88(self):
		self._getter_access_tracker["Flex88"] = {}
		return self._Flex88
	@Flex88.setter
	def Flex88(self, new_state):
		self._setter_access_tracker["Flex88"] = {}
		self._Flex88 = Flex(new_state)

	@property
	def Flex89(self):
		self._getter_access_tracker["Flex89"] = {}
		return self._Flex89
	@Flex89.setter
	def Flex89(self, new_state):
		self._setter_access_tracker["Flex89"] = {}
		self._Flex89 = Flex(new_state)

	@property
	def Image69(self):
		self._getter_access_tracker["Image69"] = {}
		return self._Image69
	@Image69.setter
	def Image69(self, new_state):
		self._setter_access_tracker["Image69"] = {}
		self._Image69 = Image(new_state)

	@property
	def Flex90(self):
		self._getter_access_tracker["Flex90"] = {}
		return self._Flex90
	@Flex90.setter
	def Flex90(self, new_state):
		self._setter_access_tracker["Flex90"] = {}
		self._Flex90 = Flex(new_state)

	@property
	def TextBox60(self):
		self._getter_access_tracker["TextBox60"] = {}
		return self._TextBox60
	@TextBox60.setter
	def TextBox60(self, new_state):
		self._setter_access_tracker["TextBox60"] = {}
		self._TextBox60 = TextBox(new_state)

	@property
	def TextBox61(self):
		self._getter_access_tracker["TextBox61"] = {}
		return self._TextBox61
	@TextBox61.setter
	def TextBox61(self, new_state):
		self._setter_access_tracker["TextBox61"] = {}
		self._TextBox61 = TextBox(new_state)

	@property
	def Flex91(self):
		self._getter_access_tracker["Flex91"] = {}
		return self._Flex91
	@Flex91.setter
	def Flex91(self, new_state):
		self._setter_access_tracker["Flex91"] = {}
		self._Flex91 = Flex(new_state)

	@property
	def Flex92(self):
		self._getter_access_tracker["Flex92"] = {}
		return self._Flex92
	@Flex92.setter
	def Flex92(self, new_state):
		self._setter_access_tracker["Flex92"] = {}
		self._Flex92 = Flex(new_state)

	@property
	def Flex93(self):
		self._getter_access_tracker["Flex93"] = {}
		return self._Flex93
	@Flex93.setter
	def Flex93(self, new_state):
		self._setter_access_tracker["Flex93"] = {}
		self._Flex93 = Flex(new_state)

	@property
	def Flex94(self):
		self._getter_access_tracker["Flex94"] = {}
		return self._Flex94
	@Flex94.setter
	def Flex94(self, new_state):
		self._setter_access_tracker["Flex94"] = {}
		self._Flex94 = Flex(new_state)

	@property
	def Image71(self):
		self._getter_access_tracker["Image71"] = {}
		return self._Image71
	@Image71.setter
	def Image71(self, new_state):
		self._setter_access_tracker["Image71"] = {}
		self._Image71 = Image(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"Flex3": self._Flex3,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"TextBox1": self._TextBox1,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"Image1": self._Image1,
			"Flex9": self._Flex9,
			"Image2": self._Image2,
			"Image3": self._Image3,
			"TextBox2": self._TextBox2,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"Button1": self._Button1,
			"Flex10": self._Flex10,
			"Flex11": self._Flex11,
			"Flex12": self._Flex12,
			"TextBox6": self._TextBox6,
			"Flex13": self._Flex13,
			"Image4": self._Image4,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"TextBox9": self._TextBox9,
			"Flex14": self._Flex14,
			"Image5": self._Image5,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"Flex17": self._Flex17,
			"TextBox10": self._TextBox10,
			"TextBox11": self._TextBox11,
			"Flex18": self._Flex18,
			"Flex19": self._Flex19,
			"TextBox12": self._TextBox12,
			"TextBox13": self._TextBox13,
			"Image11": self._Image11,
			"Image12": self._Image12,
			"Image13": self._Image13,
			"Image14": self._Image14,
			"Image15": self._Image15,
			"Flex20": self._Flex20,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"Flex23": self._Flex23,
			"Flex24": self._Flex24,
			"TextBox14": self._TextBox14,
			"TextBox15": self._TextBox15,
			"TextBox16": self._TextBox16,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Image16": self._Image16,
			"Image18": self._Image18,
			"Flex25": self._Flex25,
			"Flex26": self._Flex26,
			"Flex27": self._Flex27,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"TextBox21": self._TextBox21,
			"Button2": self._Button2,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"TextBox22": self._TextBox22,
			"Div1": self._Div1,
			"Div2": self._Div2,
			"TextBox23": self._TextBox23,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"Image21": self._Image21,
			"Image23": self._Image23,
			"Image24": self._Image24,
			"Flex36": self._Flex36,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"TextBox24": self._TextBox24,
			"TextBox25": self._TextBox25,
			"Flex39": self._Flex39,
			"Image27": self._Image27,
			"Image28": self._Image28,
			"Image30": self._Image30,
			"Image31": self._Image31,
			"Image32": self._Image32,
			"Image33": self._Image33,
			"Image34": self._Image34,
			"Image36": self._Image36,
			"Image37": self._Image37,
			"Image39": self._Image39,
			"Image40": self._Image40,
			"TextBox26": self._TextBox26,
			"Image41": self._Image41,
			"Flex40": self._Flex40,
			"TextBox27": self._TextBox27,
			"Image42": self._Image42,
			"Flex41": self._Flex41,
			"Flex42": self._Flex42,
			"Image43": self._Image43,
			"Image44": self._Image44,
			"Flex43": self._Flex43,
			"Flex44": self._Flex44,
			"Flex45": self._Flex45,
			"Flex46": self._Flex46,
			"Image45": self._Image45,
			"TextBox28": self._TextBox28,
			"Image46": self._Image46,
			"TextBox29": self._TextBox29,
			"Image47": self._Image47,
			"TextBox30": self._TextBox30,
			"Flex50": self._Flex50,
			"Flex51": self._Flex51,
			"Flex52": self._Flex52,
			"TextBox31": self._TextBox31,
			"Flex53": self._Flex53,
			"Image49": self._Image49,
			"Flex54": self._Flex54,
			"Image53": self._Image53,
			"Flex55": self._Flex55,
			"Image54": self._Image54,
			"Flex56": self._Flex56,
			"Image55": self._Image55,
			"Flex57": self._Flex57,
			"Image56": self._Image56,
			"Flex58": self._Flex58,
			"Image57": self._Image57,
			"Flex59": self._Flex59,
			"Flex60": self._Flex60,
			"Flex61": self._Flex61,
			"Image58": self._Image58,
			"Flex62": self._Flex62,
			"TextBox32": self._TextBox32,
			"TextBox33": self._TextBox33,
			"TextBox34": self._TextBox34,
			"TextBox35": self._TextBox35,
			"TextBox36": self._TextBox36,
			"Flex63": self._Flex63,
			"Image59": self._Image59,
			"TextBox37": self._TextBox37,
			"Flex64": self._Flex64,
			"Flex65": self._Flex65,
			"Flex66": self._Flex66,
			"TextBox38": self._TextBox38,
			"TextBox39": self._TextBox39,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"Image60": self._Image60,
			"Flex67": self._Flex67,
			"Flex68": self._Flex68,
			"Image61": self._Image61,
			"Flex69": self._Flex69,
			"TextBox42": self._TextBox42,
			"TextBox43": self._TextBox43,
			"Flex70": self._Flex70,
			"Flex71": self._Flex71,
			"Flex72": self._Flex72,
			"Flex73": self._Flex73,
			"TextBox44": self._TextBox44,
			"TextBox45": self._TextBox45,
			"TextBox46": self._TextBox46,
			"TextBox47": self._TextBox47,
			"Image62": self._Image62,
			"Flex74": self._Flex74,
			"Flex75": self._Flex75,
			"Image63": self._Image63,
			"Flex76": self._Flex76,
			"TextBox48": self._TextBox48,
			"TextBox49": self._TextBox49,
			"Flex77": self._Flex77,
			"Flex78": self._Flex78,
			"Flex79": self._Flex79,
			"Flex80": self._Flex80,
			"Image64": self._Image64,
			"TextBox50": self._TextBox50,
			"TextBox51": self._TextBox51,
			"TextBox52": self._TextBox52,
			"TextBox53": self._TextBox53,
			"Image65": self._Image65,
			"Image66": self._Image66,
			"Flex81": self._Flex81,
			"Flex82": self._Flex82,
			"Image67": self._Image67,
			"Flex83": self._Flex83,
			"TextBox54": self._TextBox54,
			"TextBox55": self._TextBox55,
			"Flex84": self._Flex84,
			"Flex85": self._Flex85,
			"Flex86": self._Flex86,
			"Flex87": self._Flex87,
			"TextBox56": self._TextBox56,
			"TextBox57": self._TextBox57,
			"TextBox58": self._TextBox58,
			"TextBox59": self._TextBox59,
			"Image68": self._Image68,
			"Flex88": self._Flex88,
			"Flex89": self._Flex89,
			"Image69": self._Image69,
			"Flex90": self._Flex90,
			"TextBox60": self._TextBox60,
			"TextBox61": self._TextBox61,
			"Flex91": self._Flex91,
			"Flex92": self._Flex92,
			"Flex93": self._Flex93,
			"Flex94": self._Flex94,
			"Image71": self._Image71
			}
  