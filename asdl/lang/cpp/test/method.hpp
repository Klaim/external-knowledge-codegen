struct foo {
  void bar();
  void bar(int i);
  virtual void bar(int i, int j);
  virtual void bar(int i, int j, int k) = 0;
  virtual void bar(float) final;
};
